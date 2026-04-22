"""🏆 Achievements Screen."""
import flet as ft
from theme import *
from state import get_state, ACHIEVEMENTS
from components.achievement_badge import build_badge_grid
from i18n import t

def build_achievements_screen(page):
    s = get_state()
    unlocked = len(s["achievements"])
    total = len(ACHIEVEMENTS)

    header = ft.Container(
        content=ft.Column([
            ft.Text(t("achievements_title"), size=24, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY, font_family="Bodoni", italic=True),
            ft.Text(f"{unlocked} / {total} {t('unlocked_of')}", size=14, color=TEXT_SECONDARY),
            ft.Container(
                content=ft.Stack([
                    ft.Container(height=6, border_radius=RADIUS_FULL, bgcolor=BG_ELEVATED),
                    ft.Container(
                        height=6, width=max(260 * (unlocked / max(total, 1)), 4),
                        border_radius=RADIUS_FULL, gradient=GRADIENT_ORANGE,
                    ),
                ]),
                width=260, padding=ft.padding.only(top=8),
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
        padding=PAD_SCREEN,
        alignment=ft.alignment.center,
    )

    return ft.Column([header, build_badge_grid()], spacing=0, expand=True)
