"""
🌐 DuoLearn i18n — Internationalization
Simple bilingual system (ES/EN).
"""

_lang = {"current": "es"}

STRINGS = {
    # ─── Navigation ──────────────────────────────────────────────
    "nav_home":         {"es": "Inicio",      "en": "Home"},
    "nav_achievements": {"es": "Logros",      "en": "Badges"},
    "nav_ranking":      {"es": "Ranking",     "en": "Ranking"},
    "nav_profile":      {"es": "Perfil",      "en": "Profile"},

    # ─── Home ────────────────────────────────────────────────────
    "app_title":        {"es": "🍫 Curso de Chocolatería de Autor", "en": "🍫 Artisan Chocolate Course"},
    "app_subtitle":     {"es": "Formación Dual en Chocolate Artesanal", "en": "Dual Training in Artisan Chocolate"},
    "trainer_role":     {"es": "Formador Senior Cacaotier", "en": "Senior Cacaotier Trainer"},
    "section":          {"es": "Sección",     "en": "Section"},

    # ─── XP & Level ─────────────────────────────────────────────
    "level":            {"es": "Nivel",       "en": "Level"},
    "xp":               {"es": "XP",          "en": "XP"},

    # ─── Lesson ──────────────────────────────────────────────────
    "continue":         {"es": "Continuar →", "en": "Continue →"},
    "continue_btn":     {"es": "Continuar",   "en": "Continue"},
    "no_lives":         {"es": "Sin vidas — Reintentar", "en": "No lives — Retry"},
    "lesson_complete":  {"es": "¡Lección Completada!", "en": "Lesson Complete!"},
    "correct_count":    {"es": "Correctas",   "en": "Correct"},
    "bonus":            {"es": "bonus",       "en": "bonus"},
    "level_up":         {"es": "🚀 ¡SUBISTE DE NIVEL!", "en": "🚀 LEVEL UP!"},
    "correct":          {"es": "✅ ¡Correcto!", "en": "✅ Correct!"},
    "incorrect":        {"es": "❌ Incorrecto", "en": "❌ Incorrect"},
    "true_opt":         {"es": "Verdadero ✓", "en": "True ✓"},
    "false_opt":        {"es": "Falso ✗",     "en": "False ✗"},

    # ─── Profile ─────────────────────────────────────────────────
    "total_xp":         {"es": "XP Total",    "en": "Total XP"},
    "lessons":          {"es": "Lecciones",   "en": "Lessons"},
    "best_streak":      {"es": "Mejor Racha", "en": "Best Streak"},
    "accuracy":         {"es": "Precisión",   "en": "Accuracy"},
    "achievements":     {"es": "Logros",      "en": "Badges"},
    "weekly_xp":        {"es": "XP Semanal",  "en": "Weekly XP"},
    "supported_by":     {"es": "Programa de Formación Dual", "en": "Dual Training Program"},
    "org_line":         {"es": "Chocolatería de Autor • Swisscontact", "en": "Artisan Chocolate • Swisscontact"},

    # ─── Achievements ────────────────────────────────────────────
    "achievements_title": {"es": "🏆 Logros", "en": "🏆 Badges"},
    "unlocked_of":      {"es": "desbloqueados", "en": "unlocked"},

    # ─── Leaderboard ─────────────────────────────────────────────
    "ranking_title":    {"es": "📊 Ranking Semanal", "en": "📊 Weekly Ranking"},
    "division":         {"es": "División",    "en": "Division"},
}


def get_lang():
    return _lang["current"]


def set_lang(lang: str):
    _lang["current"] = lang


def t(key: str) -> str:
    """Get translated string for current language."""
    entry = STRINGS.get(key, {})
    return entry.get(_lang["current"], entry.get("es", key))


def toggle_lang() -> str:
    """Toggle between ES and EN. Returns new lang."""
    _lang["current"] = "en" if _lang["current"] == "es" else "es"
    return _lang["current"]
