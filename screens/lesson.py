"""📝 Lesson Screen — Quiz Flow."""
import flet as ft
from theme import *
from data.curriculum import get_questions
from components.quiz_card import build_choice_question, build_tf_question, build_feedback_banner
from state import complete_lesson
from i18n import t

def build_lesson_screen(page, section_idx, lesson_idx, on_finish):
    """Full-screen quiz flow."""
    questions = get_questions(section_idx, lesson_idx)
    total_q = len(questions)

    lesson_state = {"current": 0, "hearts": 3, "correct": 0, "answered": False}

    content_area = ft.Column(spacing=16, expand=True)
    progress_bar = ft.ProgressBar(value=0, color=ACCENT_ORANGE, bgcolor=BG_ELEVATED, height=6)
    hearts_row = ft.Row(spacing=2, alignment=ft.MainAxisAlignment.END)
    question_num = ft.Text("1 / " + str(total_q), size=14, color=TEXT_SECONDARY)
    feedback_area = ft.Column(spacing=8)
    next_btn_container = ft.Column()

    def update_hearts():
        hearts_row.controls = [
            ft.Text("❤️" if i < lesson_state["hearts"] else "🖤", size=20)
            for i in range(3)
        ]

    def show_question():
        lesson_state["answered"] = False
        idx = lesson_state["current"]
        q = questions[idx]
        progress_bar.value = idx / total_q
        question_num.value = f"{idx + 1} / {total_q}"
        feedback_area.controls.clear()
        next_btn_container.controls.clear()
        update_hearts()

        if q["type"] == "choice":
            card = build_choice_question(q, on_answer_choice)
        else:
            card = build_tf_question(q, on_answer_tf)

        content_area.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.CLOSE, icon_color=TEXT_SECONDARY, icon_size=24,
                            on_click=lambda e: on_finish(None),
                        ),
                        question_num,
                        ft.Container(expand=True),
                        hearts_row,
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    progress_bar,
                ], spacing=8),
                padding=ft.padding.only(left=8, right=16, top=8, bottom=4),
            ),
            ft.Container(content=card, padding=ft.padding.symmetric(horizontal=16)),
            ft.Container(
                content=ft.Column([feedback_area, next_btn_container], spacing=12),
                padding=ft.padding.symmetric(horizontal=16),
            ),
        ]
        page.update()

    def handle_answer(is_correct, explanation):
        if lesson_state["answered"]:
            return
        lesson_state["answered"] = True

        if is_correct:
            lesson_state["correct"] += 1
        else:
            lesson_state["hearts"] = max(0, lesson_state["hearts"] - 1)

        update_hearts()
        feedback_area.controls = [build_feedback_banner(is_correct, explanation)]

        if lesson_state["hearts"] <= 0:
            next_btn_container.controls = [
                ft.Container(
                    content=ft.Text(t("no_lives"), size=16, weight=ft.FontWeight.BOLD, color=BG_PRIMARY,
                                     text_align=ft.TextAlign.CENTER),
                    padding=ft.padding.symmetric(vertical=14),
                    border_radius=RADIUS_MD, bgcolor=ACCENT_RED,
                    on_click=lambda e: restart_lesson(),
                    alignment=ft.alignment.center,
                ),
            ]
        elif lesson_state["current"] < total_q - 1:
            next_btn_container.controls = [
                ft.Container(
                    content=ft.Text(t("continue"), size=16, weight=ft.FontWeight.BOLD, color=BG_PRIMARY,
                                     text_align=ft.TextAlign.CENTER),
                    padding=ft.padding.symmetric(vertical=14),
                    border_radius=RADIUS_MD,
                    gradient=GRADIENT_ORANGE,
                    on_click=lambda e: next_question(),
                    alignment=ft.alignment.center,
                ),
            ]
        else:
            show_completion()
            return

        page.update()

    def on_answer_choice(idx):
        q = questions[lesson_state["current"]]
        handle_answer(idx == q["answer"], q["explanation"])

    def on_answer_tf(val):
        q = questions[lesson_state["current"]]
        handle_answer(val == q["answer"], q["explanation"])

    def next_question():
        lesson_state["current"] += 1
        show_question()

    def restart_lesson():
        lesson_state["current"] = 0
        lesson_state["hearts"] = 3
        lesson_state["correct"] = 0
        show_question()

    def show_completion():
        stars = lesson_state["hearts"]
        correct = lesson_state["correct"]
        result = complete_lesson(section_idx, lesson_idx, stars, correct, total_q)

        stars_display = "⭐" * stars + "☆" * (3 - stars)
        level_up_text = t("level_up") if result["leveled_up"] else ""

        content_area.controls = [
            ft.Container(expand=True),
            ft.Container(
                content=ft.Column([
                    ft.Image(src="/mascot.png", width=120, height=120, fit=ft.ImageFit.CONTAIN),
                    ft.Text(t("lesson_complete"), size=26, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                    ft.Container(height=8),
                    ft.Text(stars_display, size=40),
                    ft.Container(height=16),
                    ft.Row([
                        ft.Text(f"{t('correct_count')}: {correct}/{total_q}", size=16, color=TEXT_PRIMARY),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.Text(f"+{result['base_xp']} XP", size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                        ft.Text(f"+{result['bonus_xp']} {t('bonus')}", size=16, color=ACCENT_GREEN) if result["bonus_xp"] > 0 else ft.Container(),
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=12),
                    ft.Text(level_up_text, size=20, weight=ft.FontWeight.BOLD, color=ACCENT_GREEN) if level_up_text else ft.Container(),
                    ft.Container(height=24),
                    ft.Container(
                        content=ft.Text(t("continue_btn"), size=16, weight=ft.FontWeight.BOLD, color=BG_PRIMARY,
                                         text_align=ft.TextAlign.CENTER),
                        padding=ft.padding.symmetric(vertical=14, horizontal=48),
                        border_radius=RADIUS_MD,
                        gradient=GRADIENT_ORANGE,
                        on_click=lambda e: on_finish(result),
                        alignment=ft.alignment.center,
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                alignment=ft.alignment.center,
                padding=PAD_LG,
            ),
            ft.Container(expand=True),
        ]
        page.update()

    show_question()
    
    # Mascot Study Buddy in the corner
    mascot_buddy = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Text("¡Tú puedes!", size=14, weight=ft.FontWeight.BOLD, color=BG_PRIMARY),
                padding=ft.padding.symmetric(horizontal=12, vertical=8),
                bgcolor=TEXT_PRIMARY,
                border_radius=ft.border_radius.only(top_left=12, top_right=12, bottom_left=12, bottom_right=0),
            ),
            ft.Image(src="/mascot.png", width=80, height=80, fit=ft.ImageFit.CONTAIN),
        ], alignment=ft.MainAxisAlignment.END, cross_alignment=ft.CrossAxisAlignment.END),
        alignment=ft.alignment.bottom_right,
        padding=ft.padding.all(16),
        bottom=0, right=0,
    )

    main_stack = ft.Stack(
        controls=[
            ft.Container(content=content_area, bgcolor=BG_PRIMARY, expand=True),
            mascot_buddy
        ],
        expand=True
    )
    
    return main_stack
