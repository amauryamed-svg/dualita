"""🏠 Home Screen — Learning Path."""
import flet as ft
from theme import *
from data.curriculum import SECTIONS, total_lessons
from components.xp_bar import build_xp_bar
from components.streak_counter import build_streak_counter
from components.lesson_node import build_lesson_node, build_connector
from state import get_state, is_lesson_unlocked, is_lesson_completed
from i18n import t


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
                        ], spacing=0),
                    ], spacing=12),
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
            
            # Logos Row
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Image(src="/swisscontact_logo.png", width=90, height=24, fit=ft.ImageFit.CONTAIN),
                        ft.Container(width=1, height=16, bgcolor=BORDER_SUBTLE),
                        ft.Image(src="/caua_logo.png", width=50, height=24, fit=ft.ImageFit.CONTAIN),
                    ], spacing=16, alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Container(height=8),
                    ft.Row([
                        ft.Image(src="/sec_logo.png", width=120, height=32, fit=ft.ImageFit.CONTAIN),
                        ft.Container(width=16),
                        ft.Image(src="/bogota_logo.png", width=120, height=32, fit=ft.ImageFit.CONTAIN),
                    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ], spacing=0, alignment=ft.MainAxisAlignment.CENTER),
                padding=ft.padding.symmetric(horizontal=12, vertical=12),
                border_radius=RADIUS_MD,
                bgcolor="#FFFFFF", # White background for logos
                border=ft.border.all(1, BORDER_SUBTLE),
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
                    ft.Text("DuaLearn", size=22, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY, font_family="Bodoni", italic=True),
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
