"""
🍫 DuoLearn Theme — Chocolatería de Autor
Chocolate-inspired dark mode design system.
"""

import flet as ft

# ─── COLOR PALETTE ─────────────────────────────────────────────────
# Swiss Contact Blue Theme
BG_PRIMARY = "#0B1528"    # Very dark navy blue
BG_ELEVATED = "#132340"   # Elevated navy
BG_CARD = "#0F1C33"       # Card navy
BG_SECTION = "#16284A"    # Section navy
BORDER_SUBTLE = "#1E3661"

# Brand Accents
ACCENT_SC_BLUE = "#00539B"    # Swiss Contact Blue
ACCENT_CHOCO = "#4E342E"      # Chocolate brown
ACCENT_ORANGE = "#FF6D00"     # Vibrant orange
ACCENT_GOLD = "#FFB300"       # Vibrant amber/gold
ACCENT_RED = "#E53935"
ACCENT_GREEN = "#4CAF50"

# Text
TEXT_PRIMARY = "#F8F9FA"
TEXT_SECONDARY = "#A0ABC0"
TEXT_HINT = "#5E6C84"

STREAK_ORANGE = "#FF8C42"    # Streak flame
HEART_RED = "#FF4D6D"        # Hearts (lives)
STAR_YELLOW = "#FFD700"      # Stars rating

DIVIDER = "#2C1E12"          # Dividers

# ─── GRADIENTS ───────────────────────────────────────────────────
GRADIENT_ORANGE = ft.LinearGradient(
    begin=ft.alignment.center_left,
    end=ft.alignment.center_right,
    colors=[ACCENT_ORANGE, "#FF9100"],
)

GRADIENT_SUCCESS = ft.LinearGradient(
    begin=ft.alignment.center_left,
    end=ft.alignment.center_right,
    colors=["#58CC6B", "#45B854"],
)

GRADIENT_CARD = ft.LinearGradient(
    begin=ft.alignment.top_center,
    end=ft.alignment.bottom_center,
    colors=[BG_CARD, "#241A10"],
)

# ─── SHADOWS ─────────────────────────────────────────────────────
SHADOW_SM = ft.BoxShadow(
    spread_radius=0,
    blur_radius=8,
    color=ft.Colors.with_opacity(0.3, "#000000"),
    offset=ft.Offset(0, 2),
)

SHADOW_MD = ft.BoxShadow(
    spread_radius=0,
    blur_radius=16,
    color=ft.Colors.with_opacity(0.4, "#000000"),
    offset=ft.Offset(0, 4),
)

SHADOW_GLOW_ORANGE = ft.BoxShadow(
    spread_radius=2,
    blur_radius=20,
    color=ft.Colors.with_opacity(0.3, ACCENT_ORANGE),
    offset=ft.Offset(0, 0),
)

SHADOW_GLOW_GREEN = ft.BoxShadow(
    spread_radius=2,
    blur_radius=16,
    color=ft.Colors.with_opacity(0.25, ACCENT_GREEN),
    offset=ft.Offset(0, 0),
)

# ─── BORDER RADIUS ───────────────────────────────────────────────
RADIUS_SM = ft.border_radius.all(8)
RADIUS_MD = ft.border_radius.all(12)
RADIUS_LG = ft.border_radius.all(16)
RADIUS_XL = ft.border_radius.all(24)
RADIUS_FULL = ft.border_radius.all(100)

# ─── PADDING ─────────────────────────────────────────────────────
PAD_SM = ft.padding.all(8)
PAD_MD = ft.padding.all(16)
PAD_LG = ft.padding.all(24)
PAD_SCREEN = ft.padding.symmetric(horizontal=20, vertical=16)

# ─── TEXT STYLES ─────────────────────────────────────────────────
def title_text(value, size=28, color=TEXT_PRIMARY, weight=ft.FontWeight.W_900):
    return ft.Text(value, size=size, color=color, weight=weight, font_family="Bodoni", italic=True)

def heading_text(value, size=20, color=TEXT_PRIMARY, weight=ft.FontWeight.W_900):
    return ft.Text(value, size=size, color=color, weight=weight, font_family="Bodoni", italic=True)

def body_text(value, size=16, color=TEXT_PRIMARY, weight=ft.FontWeight.NORMAL):
    return ft.Text(value, size=size, color=color, weight=weight)

def caption_text(value, size=13, color=TEXT_SECONDARY, weight=ft.FontWeight.W_300):
    return ft.Text(value, size=size, color=color, weight=weight)

def emoji_text(value, size=32):
    return ft.Text(value, size=size)

# ─── CARD BUILDER ────────────────────────────────────────────────
def card_container(content, padding=16, border_radius=RADIUS_MD, **kwargs):
    """Standard dark card container."""
    return ft.Container(
        content=content,
        padding=padding,
        border_radius=border_radius,
        bgcolor=BG_CARD,
        border=ft.border.all(1, BORDER_SUBTLE),
        shadow=SHADOW_SM,
        **kwargs,
    )

# ─── FLET THEME OBJECT ──────────────────────────────────────────
def get_flet_theme():
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ACCENT_SC_BLUE,
            secondary=ACCENT_ORANGE,
            background=BG_PRIMARY,
            surface=BG_CARD,
            error=ACCENT_RED,
        ),
        visual_density=ft.VisualDensity.COMFORTABLE,
    )
