import flet as ft
from theme import *
from i18n import t


def build_choice_question(question, on_answer):
    """Multiple choice question card."""
    options_col = ft.Column(spacing=8)
    for i, opt in enumerate(question["options"]):
        btn = ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Text(chr(65 + i), size=14, weight=ft.FontWeight.BOLD, color=ACCENT_GOLD),
                    width=32, height=32, border_radius=RADIUS_FULL,
                    bgcolor=BG_ELEVATED, alignment=ft.alignment.center,
                ),
                ft.Text(opt, size=15, color=TEXT_PRIMARY, expand=True),
            ], spacing=12),
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=RADIUS_MD,
            bgcolor=BG_CARD,
            border=ft.border.all(1, BORDER_SUBTLE),
            on_click=lambda e, idx=i: on_answer(idx),
            ink=True,
        )
        options_col.controls.append(btn)

    return ft.Container(
        content=ft.Column([
            ft.Text(question["q"], size=18, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
            ft.Container(height=16),
            options_col,
        ], spacing=0),
        padding=PAD_LG,
        border_radius=RADIUS_LG,
        bgcolor=BG_CARD,
        border=ft.border.all(1, BORDER_SUBTLE),
        shadow=SHADOW_MD,
    )


def build_tf_question(question, on_answer):
    """True/False question card."""
    options_col = ft.Column([
        ft.Container(
            content=ft.Text(t("true_opt"), size=16, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
            padding=ft.padding.symmetric(horizontal=16, vertical=14),
            border_radius=RADIUS_SM,
            bgcolor=BG_ELEVATED,
            border=ft.border.all(1, BORDER_SUBTLE),
            on_click=lambda e: on_answer(True),
        ),
        ft.Container(
            content=ft.Text(t("false_opt"), size=16, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
            padding=ft.padding.symmetric(horizontal=16, vertical=14),
            border_radius=RADIUS_SM,
            bgcolor=BG_ELEVATED,
            border=ft.border.all(1, BORDER_SUBTLE),
            on_click=lambda e: on_answer(False),
        ),
    ], spacing=8)

    return ft.Column([
        ft.Text(question["question"], size=18, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
        ft.Container(height=8),
        options_col,
    ], spacing=4)


def build_feedback_banner(is_correct, explanation):
    """Feedback banner shown after answering."""
    color = ACCENT_GREEN if is_correct else ACCENT_RED
    return ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Text(t("correct") if is_correct else t("incorrect"), size=18, weight=ft.FontWeight.BOLD, color=color),
            ]),
            ft.Text(explanation, size=14, color=TEXT_SECONDARY),
        ], spacing=6),
        padding=PAD_MD,
        border_radius=RADIUS_MD,
        bgcolor=BG_CARD,
        border=ft.border.all(2, ACCENT_GREEN if is_correct else ACCENT_RED),
        shadow=[SHADOW_GLOW_GREEN if is_correct else SHADOW_SM],
    )
