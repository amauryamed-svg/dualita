"""Achievement badge display component."""
import flet as ft
from theme import *
from state import get_state, ACHIEVEMENTS


def build_badge(achievement, unlocked=False):
    return ft.Container(
        content=ft.Column([
            ft.Text(achievement["emoji"], size=36),
            ft.Text(
                achievement["name"], size=11,
                weight=ft.FontWeight.W_600,
                color=ACCENT_ORANGE if unlocked else TEXT_HINT,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Text(
                achievement["desc"], size=9,
                color=TEXT_SECONDARY if unlocked else TEXT_HINT,
                text_align=ft.TextAlign.CENTER,
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4,
           alignment=ft.MainAxisAlignment.CENTER),
        width=130, height=130,
        padding=8,
        border_radius=RADIUS_LG,
        bgcolor=BG_CARD if unlocked else BG_PRIMARY,
        border=ft.border.all(2, ACCENT_ORANGE if unlocked else TEXT_HINT),
        opacity=1.0 if unlocked else 0.4,
        shadow=[SHADOW_GLOW_ORANGE] if unlocked else [],
    )


def build_badge_grid():
    s = get_state()
    badges = []
    for ach in ACHIEVEMENTS:
        is_unlocked = ach["id"] in s["achievements"]
        badges.append(build_badge(ach, is_unlocked))

    return ft.GridView(
        controls=badges,
        runs_count=3,
        max_extent=140,
        child_aspect_ratio=1.0,
        spacing=12,
        run_spacing=12,
        padding=PAD_MD,
        expand=True,
    )
