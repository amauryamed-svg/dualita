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
    
    def close_bs(e):
        bs.open = False
        page.update()

    schedule_rows = []
    for item in mooc.get("schedule", []):
        schedule_rows.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(item["period"], weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                    ft.Row([
                        ft.Icon(ft.Icons.WB_SUN_OUTLINE, size=16, color=TEXT_SECONDARY),
                        ft.Text(item["morning"], size=13, color=TEXT_PRIMARY),
                    ], spacing=8),
                    ft.Row([
                        ft.Icon(ft.Icons.NIGHTLIGHT_ROUND, size=16, color=TEXT_SECONDARY),
                        ft.Text(item["afternoon"], size=13, color=TEXT_PRIMARY),
                    ], spacing=8),
                ], spacing=4),
                padding=12,
                border_radius=8,
                bgcolor=BG_ELEVATED,
                border=ft.border.all(1, BORDER_SUBTLE),
            )
        )

    bs = ft.BottomSheet(
        ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"{section['emoji']} {section['title']}", size=20, weight=ft.FontWeight.BOLD),
                    ft.IconButton(ft.Icons.CLOSE, on_click=close_bs),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Divider(color=BORDER_SUBTLE),
                ft.Text("MICRO MOOC INTRODUCCIÓN", size=12, weight=ft.FontWeight.W_900, color=ACCENT_ORANGE),
                ft.Text(mooc.get("intro", ""), size=15, color=TEXT_PRIMARY),
                ft.Container(height=16),
                ft.Text("CRONOGRAMA DE CLASE", size=12, weight=ft.FontWeight.W_900, color=ACCENT_ORANGE),
                ft.Column(schedule_rows, spacing=8, scroll=ft.ScrollMode.AUTO),
                ft.Container(height=20),
            ], tight=True, spacing=12),
            padding=24,
            bgcolor=BG_CARD,
            border_radius=ft.border_radius.only(top_left=24, top_right=24),
        ),
        open=True,
    )
    page.overlay.append(bs)
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

    # ─── Hero banner: Profile + Logos ────────────────────
    hero_banner = ft.Container(
        content=ft.Column([
            ft.Row([
                # Profile photo
                ft.Container(
                    content=ft.Image(
                        src="/profile_photo.png",
                        width=52, height=52,
                        fit=ft.ImageFit.COVER,
                    ),
                    width=56, height=56,
                    border_radius=RADIUS_FULL,
                    bgcolor="#FFFFFF",
                    border=ft.border.all(2, ACCENT_ORANGE),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    alignment=ft.alignment.center,
                ),
                # Instructor info
                ft.Column([
                    ft.Text(t("trainer_role"), size=11, color=TEXT_SECONDARY, weight=ft.FontWeight.W_300),
                    ft.Text(get_state()["name"], size=15, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                ], spacing=1, expand=True),
            ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            
            ft.Container(height=8),
            
            ft.Container(
                content=ft.Row([
                    ft.Image(src="/swisscontact_logo.svg", width=120, height=32, fit=ft.ImageFit.CONTAIN),
                ], spacing=0, alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.symmetric(horizontal=12, vertical=12),
                border_radius=RADIUS_MD,
                bgcolor="#FFFFFF",
                border=ft.border.all(1, BORDER_SUBTLE),
                margin=ft.margin.symmetric(horizontal=40),
            ),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=16, vertical=12),
        border_radius=RADIUS_MD,
        bgcolor=BG_CARD,
        border=ft.border.all(1, BORDER_SUBTLE),
        margin=ft.margin.only(bottom=8),
    )

    # Header
    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Row([
                    ft.Image(src="/mascot.png", width=28, height=28, fit=ft.ImageFit.CONTAIN),
                    ft.Text("Dualita", size=22, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY, font_family="Bodoni", italic=True),
                ], spacing=8, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.Icons.LANGUAGE,
                    icon_color=TEXT_SECONDARY,
                    tooltip="Toggle ES/EN",
                    on_click=on_toggle_lang,
                ),
                build_streak_counter(),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Text(t("app_subtitle"), size=13, color=TEXT_SECONDARY),
            ft.Container(height=8),
            hero_banner,
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
