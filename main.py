"""
🍫 DuoLearn — Chocolatería de Autor
Gamified learning app for artisan chocolate dual training.
"""

import flet as ft
from theme import *
from state import load_state, save_state
from i18n import t, toggle_lang, get_lang
from screens.home import build_home_screen
from screens.lesson import build_lesson_screen
from screens.profile import build_profile_screen
from screens.achievements import build_achievements_screen
from screens.leaderboard import build_leaderboard_screen


def main(page: ft.Page):
    page.title = "Dualita — Curso de Chocolatería de Autor"
    page.bgcolor = BG_PRIMARY
    page.theme_mode = ft.ThemeMode.DARK
    page.fonts = {
        "Bodoni": "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@1,6..96,900&display=swap"
    }
    page.theme = get_flet_theme()
    page.padding = 0
    page.spacing = 0
    
    # Try setting window icon (Flet 0.28+ syntax)
    try:
        page.window.icon = "/mascot.png"
    except AttributeError:
        pass # Ignore if older Flet version

    load_state()

    current_tab = {"index": 0}
    content_area = ft.Container(expand=True, bgcolor=BG_PRIMARY)

    def refresh_screen():
        idx = current_tab["index"]
        if idx == 0:
            content_area.content = build_home_screen(page, start_lesson, on_toggle_lang)
        elif idx == 1:
            content_area.content = build_achievements_screen(page)
        elif idx == 2:
            content_area.content = build_leaderboard_screen(page)
        elif idx == 3:
            content_area.content = build_profile_screen(page)

        # Update nav labels
        nav = page.navigation_bar
        nav.destinations[0].label = t("nav_home")
        nav.destinations[1].label = t("nav_achievements")
        nav.destinations[2].label = t("nav_ranking")
        nav.destinations[3].label = t("nav_profile")
        page.update()

    def on_nav_change(e):
        current_tab["index"] = e.control.selected_index
        refresh_screen()

    def on_toggle_lang(e):
        toggle_lang()
        refresh_screen()

    def start_lesson(section_idx, lesson_idx):
        page.navigation_bar.visible = False
        content_area.content = build_lesson_screen(
            page, section_idx, lesson_idx, on_finish=finish_lesson
        )
        page.update()

    def finish_lesson(result):
        page.navigation_bar.visible = True
        current_tab["index"] = 0
        page.navigation_bar.selected_index = 0
        refresh_screen()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label=t("nav_home")),
            ft.NavigationBarDestination(icon=ft.Icons.EMOJI_EVENTS_OUTLINED, selected_icon=ft.Icons.EMOJI_EVENTS, label=t("nav_achievements")),
            ft.NavigationBarDestination(icon=ft.Icons.LEADERBOARD_OUTLINED, selected_icon=ft.Icons.LEADERBOARD, label=t("nav_ranking")),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINED, selected_icon=ft.Icons.PERSON, label=t("nav_profile")),
        ],
        on_change=on_nav_change,
        bgcolor=BG_CARD,
        indicator_color=ACCENT_GOLD,
        selected_index=0,
    )

    content_area.content = build_home_screen(page, start_lesson, on_toggle_lang)
    page.add(content_area)


ft.app(target=main, assets_dir="assets")
