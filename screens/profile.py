"""👤 Profile Screen."""
import flet as ft
from theme import *
from state import get_state, xp_progress_fraction, xp_for_next_level
from components.xp_bar import build_xp_bar
from i18n import t


def build_profile_screen(page):
    s = get_state()

    def stat_card(emoji, label, value):
        return ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=28),
                ft.Text(str(value), size=22, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                ft.Text(label, size=11, color=TEXT_SECONDARY, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4,
               alignment=ft.MainAxisAlignment.CENTER),
            expand=True, height=110,
            padding=12, border_radius=RADIUS_MD,
            bgcolor=BG_CARD, border=ft.border.all(1, BORDER_SUBTLE),
        )

    accuracy = round(s["total_correct"] / max(s["total_questions"], 1) * 100)

    return ft.ListView(
        controls=[
            ft.Container(height=20),
            # Profile photo + Name
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Image(
                            src="/profile_photo.png",
                            width=110, height=110,
                            fit=ft.ImageFit.COVER,
                        ),
                        width=116, height=116,
                        border_radius=RADIUS_FULL,
                        border=ft.border.all(3, ACCENT_ORANGE),
                        shadow=SHADOW_GLOW_ORANGE,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        alignment=ft.alignment.center,
                    ),
                    ft.Text(s["name"], size=26, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                    ft.Container(
                        content=ft.Text(
                            t("trainer_role"),
                            size=13, weight=ft.FontWeight.W_600, color=ACCENT_ORANGE,
                        ),
                        padding=ft.padding.symmetric(horizontal=14, vertical=4),
                        border_radius=RADIUS_FULL,
                        bgcolor=BG_ELEVATED,
                        border=ft.border.all(1, ACCENT_ORANGE),
                    ),
                    ft.Text(f"{t('level')} {s['level']}", size=14, color=TEXT_SECONDARY),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=16),
            ),

            # Affiliation card
            ft.Container(
                content=ft.Column([
                    ft.Text(t("supported_by"), size=13, weight=ft.FontWeight.W_600, color=TEXT_PRIMARY),
                    ft.Text(t("org_line"), size=11, color=TEXT_SECONDARY),
                    ft.Container(height=8),
                    ft.Row([
                        ft.Image(src="/swisscontact_logo.svg", width=140, height=40, fit=ft.ImageFit.CONTAIN),
                    ], spacing=0, alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ], spacing=4, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.symmetric(horizontal=16, vertical=16),
                margin=ft.margin.symmetric(horizontal=16),
                border_radius=RADIUS_MD,
                bgcolor="#FFFFFF", # Force white background for dark transparent logos
                border=ft.border.all(1, BORDER_SUBTLE),
            ),

            ft.Container(height=16),
            # XP Bar
            ft.Container(content=build_xp_bar(), padding=ft.padding.symmetric(horizontal=16)),
            ft.Container(height=16),
            # Stats Grid
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        stat_card("⚡", t("total_xp"), s["xp"]),
                        stat_card("📚", t("lessons"), len(s["lessons_completed"])),
                    ], spacing=12),
                    ft.Row([
                        stat_card("🔥", t("best_streak"), s["best_streak"]),
                        stat_card("🎯", t("accuracy"), f"{accuracy}%"),
                    ], spacing=12),
                    ft.Row([
                        stat_card("🏆", t("achievements"), len(s["achievements"])),
                        stat_card("📊", t("weekly_xp"), s["weekly_xp"]),
                    ], spacing=12),
                ], spacing=12),
                padding=ft.padding.symmetric(horizontal=16),
            ),
            ft.Container(height=100),
        ],
        expand=True,
        padding=ft.padding.symmetric(horizontal=4),
    )
