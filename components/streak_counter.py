"""Streak flame counter component."""
import flet as ft
from theme import *
from state import get_state


def build_streak_counter():
    s = get_state()
    streak = s["streak"]
    has_streak = streak > 0

    return ft.Container(
        content=ft.Row([
            ft.Text("🔥", size=22),
            ft.Text(
                str(streak),
                size=18, weight=ft.FontWeight.BOLD,
                color=STREAK_ORANGE if has_streak else TEXT_HINT,
            ),
        ], spacing=4, alignment=ft.MainAxisAlignment.CENTER),
        padding=ft.padding.symmetric(horizontal=12, vertical=6),
        border_radius=RADIUS_FULL,
        bgcolor=BG_CARD,
        border=ft.border.all(1, STREAK_ORANGE if has_streak else BORDER_SUBTLE),
    )
