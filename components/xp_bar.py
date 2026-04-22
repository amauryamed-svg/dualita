"""XP progress bar component."""
import flet as ft
from theme import *
from state import get_state, xp_for_next_level, xp_progress_fraction
from i18n import t


def build_xp_bar():
    s = get_state()
    frac = xp_progress_fraction()
    threshold = xp_for_next_level(s["level"])
    prev = sum(i * 300 for i in range(1, s["level"]))
    current = s["xp"] - prev

    return ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Text("⚡", size=18),
                ft.Text(f"{t('level')} {s['level']}", size=14, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                ft.Container(expand=True),
                ft.Text(f"{current}/{threshold} XP", size=12, color=TEXT_SECONDARY),
            ], alignment=ft.MainAxisAlignment.START),
            ft.Container(
                content=ft.Stack([
                    ft.Container(width=260, height=10, border_radius=RADIUS_FULL, bgcolor=BG_ELEVATED),
                    ft.Container(
                        width=max(260 * frac, 4), height=10,
                        border_radius=RADIUS_FULL,
                        gradient=GRADIENT_ORANGE,
                    ),
                ]),
                padding=ft.padding.only(top=4),
            ),
        ], spacing=2),
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        border_radius=RADIUS_MD,
        bgcolor=BG_CARD,
        border=ft.border.all(1, BORDER_SUBTLE),
    )
