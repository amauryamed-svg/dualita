"""📊 Leaderboard Screen."""
import flet as ft
import random
from theme import *
from state import get_state
from i18n import t

BOTS = [
    ("María C.", "🇨🇴"), ("Carlos R.", "🇲🇽"), ("Ana P.", "🇪🇨"),
    ("Diego M.", "🇵🇪"), ("Laura S.", "🇻🇪"), ("Pedro G.", "🇨🇷"),
    ("Sofía L.", "🇨🇴"), ("Juan D.", "🇲🇽"), ("Isabella T.", "🇪🇨"),
]

DIVISIONS = [
    {"name": "Bronce", "emoji": "🥉", "min": 0},
    {"name": "Plata", "emoji": "🥈", "min": 500},
    {"name": "Oro", "emoji": "🥇", "min": 2000},
    {"name": "Diamante", "emoji": "💎", "min": 5000},
]

def build_leaderboard_screen(page):
    s = get_state()
    user_weekly = s["weekly_xp"]

    div = DIVISIONS[0]
    for d in DIVISIONS:
        if s["xp"] >= d["min"]:
            div = d

    random.seed(42)
    entries = []
    for name, flag in BOTS:
        xp = random.randint(max(0, user_weekly - 200), user_weekly + 300)
        entries.append({"name": f"{flag} {name}", "xp": xp, "is_user": False})

    entries.append({"name": f"🍫 {s['name']}", "xp": user_weekly, "is_user": True})
    entries.sort(key=lambda x: x["xp"], reverse=True)

    rows = []
    for i, entry in enumerate(entries):
        rank = i + 1
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"#{rank}"
        is_user = entry["is_user"]

        rows.append(
            ft.Container(
                content=ft.Row([
                    ft.Text(medal, size=18, width=40),
                    ft.Text(
                        entry["name"], size=15,
                        weight=ft.FontWeight.BOLD if is_user else ft.FontWeight.NORMAL,
                        color=ACCENT_ORANGE if is_user else TEXT_PRIMARY,
                        expand=True,
                    ),
                    ft.Text(
                        f"{entry['xp']} XP", size=14,
                        color=ACCENT_ORANGE if is_user else TEXT_SECONDARY,
                        weight=ft.FontWeight.BOLD if is_user else ft.FontWeight.NORMAL,
                    ),
                ], alignment=ft.MainAxisAlignment.START),
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                border_radius=RADIUS_MD,
                bgcolor=BG_ELEVATED if is_user else BG_CARD,
                border=ft.border.all(2, ACCENT_ORANGE) if is_user else ft.border.all(1, BORDER_SUBTLE),
                shadow=[SHADOW_GLOW_ORANGE] if is_user else [],
            )
        )

    header = ft.Container(
        content=ft.Column([
            ft.Text(t("ranking_title"), size=24, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY, font_family="Bodoni", italic=True),
            ft.Container(
                content=ft.Row([
                    ft.Text(div["emoji"], size=24),
                    ft.Text(f"{t('division')} {div['name']}", size=16, weight=ft.FontWeight.W_600, color=ACCENT_ORANGE),
                ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                padding=ft.padding.symmetric(horizontal=20, vertical=8),
                border_radius=RADIUS_FULL, bgcolor=BG_CARD,
                border=ft.border.all(1, ACCENT_ORANGE),
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=12),
        padding=PAD_SCREEN,
    )

    return ft.Column([
        header,
        ft.ListView(controls=rows, expand=True, spacing=8, padding=ft.padding.symmetric(horizontal=16)),
    ], spacing=0, expand=True)
