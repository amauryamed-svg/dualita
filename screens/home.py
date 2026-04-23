"""🏠 Home Screen — Learning Path."""
import flet as ft
from theme import *
from data.curriculum import SECTIONS, total_lessons
from components.xp_bar import build_xp_bar
from components.streak_counter import build_streak_counter
from components.lesson_node import build_lesson_node, build_connector
from state import get_state, is_lesson_unlocked, is_lesson_completed
from i18n import t


def show_mooc_info(page, section):
    mooc = section.get("mooc", {})
    
    def close_dlg(e):
        page.close(dlg)

    def download_recipe(e):
        page.launch_url(mooc.get("recipe_url", "#"))

    # Schedule Section
    schedule_rows = []
    for item in mooc.get("schedule", []):
        schedule_rows.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(item["period"], weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE, size=13),
                    ft.Row([
                        ft.Icon(ft.Icons.WB_SUN_OUTLINE, size=14, color=TEXT_SECONDARY),
                        ft.Text(item["morning"], size=11, color=TEXT_PRIMARY),
                    ], spacing=8),
                    ft.Row([
                        ft.Icon(ft.Icons.NIGHTLIGHT_ROUND, size=14, color=TEXT_SECONDARY),
                        ft.Text(item["afternoon"], size=11, color=TEXT_PRIMARY),
                    ], spacing=8),
                ], spacing=2),
                padding=8, border_radius=8, bgcolor=BG_ELEVATED, border=ft.border.all(1, BORDER_SUBTLE),
            )
        )

    # Step-by-step Section
    step_controls = []
    for i, step in enumerate(mooc.get("steps", [])):
        step_controls.append(
            ft.Row([
                ft.Container(
                    content=ft.Text(str(i+1), color="#FFFFFF", size=10, weight=ft.FontWeight.BOLD),
                    width=20, height=20, border_radius=10, bgcolor=ACCENT_ORANGE, alignment=ft.alignment.center
                ),
                ft.Text(step, size=13, color=TEXT_PRIMARY, expand=True),
            ], vertical_alignment=ft.CrossAxisAlignment.START, spacing=10)
        )

    dlg = ft.AlertDialog(
        modal=False,
        title=ft.Row([
            ft.Text(f"{section['emoji']} {section['title']}", size=18, weight=ft.FontWeight.BOLD),
            ft.IconButton(ft.Icons.CLOSE, on_click=close_dlg, icon_size=20),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        content=ft.Container(
            content=ft.Column([
                ft.Divider(color=BORDER_SUBTLE, height=1),
                ft.Text("MICRO MOOC INTRODUCCIÓN", size=10, weight=ft.FontWeight.W_900, color=ACCENT_ORANGE),
                ft.Text(mooc.get("intro", ""), size=13, color=TEXT_PRIMARY),
                
                ft.Container(height=10),
                ft.Text("PASO A PASO DE LA CLASE", size=10, weight=ft.FontWeight.W_900, color=ACCENT_ORANGE),
                ft.Column(step_controls, spacing=8),

                ft.Container(height=10),
                ft.Text("CRONOGRAMA MENSUAL", size=10, weight=ft.FontWeight.W_900, color=ACCENT_ORANGE),
                ft.Column(schedule_rows, spacing=4),
                
                ft.Container(height=10),
                ft.ElevatedButton(
                    "Descargar Recetario PDF",
                    icon=ft.Icons.PICTURE_AS_PDF,
                    color="#FFFFFF",
                    bgcolor=ACCENT_ORANGE,
                    on_click=download_recipe,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                ),
            ], tight=True, spacing=8, scroll=ft.ScrollMode.AUTO),
            width=400,
            max_height=500,
        ),
        bgcolor=BG_CARD,
        shape=ft.RoundedRectangleBorder(radius=RADIUS_LG),
    )
    
    page.open(dlg)
    page.update()


def build_home_screen(page, on_start_lesson, on_toggle_lang):
    """Build the home screen with learning path."""

    def build_path():
        s = get_state()
        path_controls = []

        for sec_idx, section in enumerate(SECTIONS):
            # Section header
            path_controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Text(section["emoji"], size=24),
                        ft.Column([
                            ft.Text(f"{t('section')} {sec_idx + 1}", size=11, color=TEXT_SECONDARY, weight=ft.FontWeight.W_300),
                            ft.Text(section["title"], size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                        ], spacing=0, expand=True),
                        ft.IconButton(
                            icon=ft.Icons.INFO_OUTLINE,
                            icon_color=ACCENT_ORANGE,
                            tooltip="Micro MOOC Info",
                            on_click=lambda e, s=section: show_mooc_info(page, s),
                        ),
                    ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=ft.padding.symmetric(horizontal=16, vertical=10),
                    margin=ft.margin.only(top=16 if sec_idx > 0 else 0, bottom=4),
                    border_radius=RADIUS_MD,
                    bgcolor=BG_SECTION,
                    border=ft.border.all(1, BORDER_SUBTLE),
                    on_click=lambda e, s=section: show_mooc_info(page, s),
                )
            )

            n_lessons = total_lessons(sec_idx)
            for les_idx in range(n_lessons):
                lesson = section["lessons"][les_idx]
                is_current = is_lesson_unlocked(sec_idx, les_idx) and not is_lesson_completed(sec_idx, les_idx)

                if is_current:
                    for prev_s in range(len(SECTIONS)):
                        found_earlier = False
                        limit = total_lessons(prev_s)
                        for prev_l in range(limit):
                            if prev_s == sec_idx and prev_l >= les_idx:
                                break
                            if is_lesson_unlocked(prev_s, prev_l) and not is_lesson_completed(prev_s, prev_l):
                                is_current = False
                                found_earlier = True
                                break
                        if found_earlier or (prev_s == sec_idx):
                            break

                node = build_lesson_node(
                    sec_idx, les_idx, lesson["title"],
                    on_tap=lambda e, si=sec_idx, li=les_idx: on_start_lesson(si, li),
                    is_current=is_current,
                )

                offset = 40 if (sec_idx * 4 + les_idx) % 2 == 0 else -40
                path_controls.append(
                    ft.Container(content=node, alignment=ft.alignment.center,
                                 margin=ft.margin.only(left=offset + 80))
                )

                if not (sec_idx == len(SECTIONS) - 1 and les_idx == n_lessons - 1):
                    path_controls.append(ft.Container(content=build_connector(), alignment=ft.alignment.center))

        # Add Dua the Mascot at the end of the path
        path_controls.append(
            ft.Container(
                content=ft.Image(src="/mascot.png", width=120, height=120, fit=ft.ImageFit.CONTAIN),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=32, bottom=32),
            )
        )

        return path_controls

    # Intro Greeting & Motivation
    intro_banner = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Image(src="/mascot.png", width=70, height=70, fit=ft.ImageFit.CONTAIN),
                ft.Column([
                    ft.Text("¡Hola, Chocolover!", size=14, color=ACCENT_ORANGE, weight=ft.FontWeight.W_600),
                    ft.Text("¡Bienvenido a Dualita!", size=28, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY, font_family="Bodoni", italic=True),
                ], spacing=0),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=16),
            ft.Text(
                "Estás en el camino hacia la excelencia. Cada lección es un paso más para convertirte en un experto de la chocolatería de autor.",
                size=14, color=TEXT_SECONDARY, italic=True
            ),
            ft.Container(height=4),
            # Instructor info small card
            ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Image(src="/profile_photo.png", width=40, height=40, fit=ft.ImageFit.COVER),
                        width=44, height=44, border_radius=RADIUS_FULL,
                        bgcolor="#FFFFFF", border=ft.border.all(1, ACCENT_ORANGE),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS, alignment=ft.alignment.center,
                    ),
                    ft.Column([
                        ft.Text(t("trainer_role"), size=10, color=TEXT_SECONDARY, weight=ft.FontWeight.W_300),
                        ft.Text(get_state()["name"], size=13, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                    ], spacing=0),
                    ft.Container(expand=True),
                    ft.Image(src="/swisscontact_logo.svg", width=80, height=20, fit=ft.ImageFit.CONTAIN),
                ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.all(10),
                border_radius=RADIUS_MD,
                bgcolor=BG_ELEVATED,
                border=ft.border.all(1, BORDER_SUBTLE),
            ),
        ], spacing=12),
        padding=ft.padding.all(20),
        border_radius=RADIUS_LG,
        bgcolor=BG_CARD,
        border=ft.border.all(1, BORDER_SUBTLE),
        margin=ft.margin.only(bottom=16),
        shadow=SHADOW_MD,
    )

    # Header
    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.Icons.LANGUAGE,
                    icon_color=TEXT_SECONDARY,
                    tooltip="Toggle ES/EN",
                    on_click=on_toggle_lang,
                ),
                build_streak_counter(),
            ], alignment=ft.MainAxisAlignment.END),
            intro_banner,
            build_xp_bar(),
        ]),
        padding=PAD_SCREEN,
        bgcolor=BG_PRIMARY,
    )

    path_controls = build_path()
    path_view = ft.ListView(
        controls=path_controls, expand=True,
        padding=ft.padding.only(bottom=100, top=8, left=8, right=8), spacing=0,
    )

    return ft.Column([header, path_view], spacing=0, expand=True)
