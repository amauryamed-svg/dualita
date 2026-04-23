"""📚 Curriculum View — Plan de Formación Dual."""
import flet as ft
from theme import *
from data.curriculum import SECTIONS
from i18n import t

def build_curriculum_view(page):
    
    def section_card(section):
        mooc = section.get("mooc", {})
        
        # Schedule rows
        schedule_rows = []
        for item in mooc.get("schedule", []):
            schedule_rows.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(item["period"], weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE, size=13),
                        ft.Row([
                            ft.Icon(ft.Icons.LIGHT_MODE, size=14, color=TEXT_SECONDARY),
                            ft.Text(item["morning"], size=11, color=TEXT_PRIMARY),
                        ], spacing=8),
                        ft.Row([
                            ft.Icon(ft.Icons.NIGHTLIGHT, size=14, color=TEXT_SECONDARY),
                            ft.Text(item["afternoon"], size=11, color=TEXT_PRIMARY),
                        ], spacing=8),
                    ], spacing=2),
                    padding=10, border_radius=8, bgcolor=BG_ELEVATED, border=ft.border.all(1, BORDER_SUBTLE),
                )
            )

        # Step rows
        step_rows = []
        for i, step in enumerate(mooc.get("steps", [])):
            step_rows.append(
                ft.Row([
                    ft.Container(
                        content=ft.Text(str(i+1), color="#FFFFFF", size=10, weight=ft.FontWeight.BOLD),
                        width=20, height=20, border_radius=10, bgcolor=ACCENT_ORANGE, alignment=ft.alignment.center
                    ),
                    ft.Text(step, size=13, color=TEXT_PRIMARY, expand=True),
                ], vertical_alignment=ft.CrossAxisAlignment.START, spacing=10)
            )

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(section["emoji"], size=28),
                    ft.Text(section["title"], size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE, expand=True),
                ], spacing=12),
                ft.Divider(color=BORDER_SUBTLE, height=1),
                
                ft.Text("INTRODUCCIÓN AL MÓDULO", size=10, weight=ft.FontWeight.W_900, color=TEXT_SECONDARY),
                ft.Text(mooc.get("intro", ""), size=14, color=TEXT_PRIMARY),
                
                ft.Container(height=8),
                ft.Text("PASO A PASO DE LA CLASE", size=10, weight=ft.FontWeight.W_900, color=TEXT_SECONDARY),
                ft.Column(step_rows, spacing=6),

                ft.Container(height=8),
                ft.Text("CRONOGRAMA DE FORMACIÓN", size=10, weight=ft.FontWeight.W_900, color=TEXT_SECONDARY),
                ft.Column(schedule_rows, spacing=6),
                
                ft.Container(height=12),
                ft.ElevatedButton(
                    "Descargar Recetario PDF",
                    icon=ft.Icons.PICTURE_AS_PDF,
                    color="#FFFFFF",
                    bgcolor=ACCENT_ORANGE,
                    on_click=lambda _: page.launch_url(mooc.get("recipe_url", "#")),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    width=220,
                ),
            ], spacing=12),
            padding=20,
            border_radius=RADIUS_LG,
            bgcolor=BG_CARD,
            border=ft.border.all(1, BORDER_SUBTLE),
            margin=ft.margin.only(bottom=16),
        )

    cards = [section_card(s) for s in SECTIONS]
    
    return ft.Column([
        ft.Container(
            content=ft.Column([
                ft.Text("Plan de Formación Dual", size=28, weight=ft.FontWeight.W_900, color=TEXT_PRIMARY, font_family="Bodoni", italic=True),
                ft.Text("Micro MOOCs: Guía de clases presenciales, cronogramas y recetarios.", size=14, color=TEXT_SECONDARY),
            ], spacing=4),
            padding=ft.padding.only(left=20, right=20, top=20, bottom=10),
        ),
        ft.ListView(
            controls=cards,
            expand=True,
            padding=ft.padding.only(left=16, right=16, bottom=100),
            spacing=0,
        )
    ], expand=True, spacing=0)
