"""Learning path lesson node component."""
import flet as ft
from theme import *
from state import is_lesson_unlocked, is_lesson_completed, get_lesson_stars


def build_lesson_node(section_idx, lesson_idx, title, on_tap, is_current=False):
    completed = is_lesson_completed(section_idx, lesson_idx)
    unlocked = is_lesson_unlocked(section_idx, lesson_idx)
    stars = get_lesson_stars(section_idx, lesson_idx)

    if completed:
        bg = BG_CARD
        border_color = ACCENT_ORANGE
        icon_emoji = "✅"
        opacity = 1.0
        shadow = [SHADOW_SM]
        star_row = ft.Row(
            [ft.Text("⭐" * stars + "☆" * (3 - stars), size=12)],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    elif unlocked:
        bg = BG_ELEVATED if not is_current else BG_CARD
        border_color = ACCENT_ORANGE if is_current else ACCENT_AMBER
        icon_emoji = "▶️" if is_current else "📖"
        opacity = 1.0
        shadow = [SHADOW_GLOW_ORANGE] if is_current else [SHADOW_SM]
        star_row = ft.Container()
    else:
        bg = BG_PRIMARY
        border_color = TEXT_HINT
        icon_emoji = "🔒"
        opacity = 0.5
        shadow = []
        star_row = ft.Container()

    node = ft.Container(
        content=ft.Column([
            ft.Text(icon_emoji, size=28),
            ft.Text(
                title, size=12, color=TEXT_PRIMARY if unlocked else TEXT_HINT,
                weight=ft.FontWeight.W_600 if is_current else ft.FontWeight.NORMAL,
                text_align=ft.TextAlign.CENTER,
            ),
            star_row,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
        width=110, height=110,
        alignment=ft.alignment.center,
        padding=8,
        border_radius=RADIUS_LG,
        bgcolor=bg,
        border=ft.border.all(2, border_color),
        opacity=opacity,
        shadow=shadow,
        on_click=on_tap if unlocked else None,
        animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
    )
    return node


def build_connector():
    """Dotted vertical connector between nodes."""
    return ft.Container(
        content=ft.Column([
            ft.Container(width=2, height=6, bgcolor=TEXT_HINT, border_radius=RADIUS_FULL),
            ft.Container(width=2, height=6, bgcolor=TEXT_HINT, border_radius=RADIUS_FULL),
            ft.Container(width=2, height=6, bgcolor=TEXT_HINT, border_radius=RADIUS_FULL),
        ], spacing=3, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        height=30,
        alignment=ft.alignment.center,
    )
