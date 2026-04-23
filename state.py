"""
🧠 DuoLearn State — User progress & persistence
"""

import json
import os
from datetime import datetime, date

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data.json")

# ─── DEFAULT STATE ───────────────────────────────────────────────
DEFAULT_STATE = {
    "name": "Amaury Amed",
    "xp": 0,
    "level": 1,
    "streak": 0,
    "best_streak": 0,
    "last_played": None,
    "lessons_completed": {},      # {"section_lesson": stars}
    "achievements": [],           # List of unlocked achievement IDs
    "total_correct": 0,
    "total_questions": 0,
    "weekly_xp": 0,
    "week_start": None,
}

# ─── GLOBAL STATE ────────────────────────────────────────────────
_state = {}


def load_state():
    """Load user state from JSON file, or initialize defaults."""
    global _state
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                _state = json.load(f)
            # Merge any new keys from DEFAULT_STATE
            for key, val in DEFAULT_STATE.items():
                if key not in _state:
                    _state[key] = val
        except (json.JSONDecodeError, IOError):
            _state = DEFAULT_STATE.copy()
    else:
        _state = DEFAULT_STATE.copy()
    return _state


def save_state():
    """Persist current state to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(_state, f, indent=2, ensure_ascii=False)


def get_state():
    """Get reference to current state dict."""
    if not _state:
        load_state()
    return _state


# ─── XP & LEVELS ─────────────────────────────────────────────────
def xp_for_next_level(level: int) -> int:
    """XP required to reach the NEXT level."""
    return level * 300


def xp_progress_fraction() -> float:
    """Progress toward next level as 0.0–1.0."""
    s = get_state()
    threshold = xp_for_next_level(s["level"])
    # XP accumulated within current level
    prev_threshold = sum(i * 300 for i in range(1, s["level"]))
    current_xp = s["xp"] - prev_threshold
    return min(max(current_xp / threshold, 0), 1.0)


def add_xp(amount: int) -> dict:
    """
    Add XP and check for level-up.
    Returns {"leveled_up": bool, "new_level": int, "xp_gained": int}
    """
    s = get_state()
    s["xp"] += amount
    s["weekly_xp"] += amount
    leveled_up = False

    while True:
        prev_threshold = sum(i * 300 for i in range(1, s["level"]))
        next_threshold = prev_threshold + xp_for_next_level(s["level"])
        if s["xp"] >= next_threshold:
            s["level"] += 1
            leveled_up = True
        else:
            break

    save_state()
    return {"leveled_up": leveled_up, "new_level": s["level"], "xp_gained": amount}


# ─── STREAKS ─────────────────────────────────────────────────────
def update_streak():
    """Update streak based on last played date."""
    s = get_state()
    today = date.today().isoformat()

    if s["last_played"] is None:
        s["streak"] = 1
    elif s["last_played"] == today:
        pass  # Already played today
    else:
        last = date.fromisoformat(s["last_played"])
        diff = (date.today() - last).days
        if diff == 1:
            s["streak"] += 1
        elif diff > 1:
            s["streak"] = 1  # Streak broken

    s["last_played"] = today
    if s["streak"] > s["best_streak"]:
        s["best_streak"] = s["streak"]

    # Reset weekly XP if new week
    if s["week_start"] is None:
        s["week_start"] = today
    else:
        week_start_date = date.fromisoformat(s["week_start"])
        if (date.today() - week_start_date).days >= 7:
            s["weekly_xp"] = 0
            s["week_start"] = today

    save_state()


# ─── LESSONS ─────────────────────────────────────────────────────
def complete_lesson(section_idx: int, lesson_idx: int, stars: int, correct: int, total: int):
    """
    Mark a lesson as completed.
    Returns XP earned (including bonus).
    """
    s = get_state()
    key = f"{section_idx}_{lesson_idx}"

    base_xp = correct * 50
    bonus = 100 if correct == total else 0
    total_xp = base_xp + bonus

    # Only update if better stars
    prev_stars = s["lessons_completed"].get(key, 0)
    if stars > prev_stars:
        s["lessons_completed"][key] = stars

    s["total_correct"] += correct
    s["total_questions"] += total

    update_streak()
    result = add_xp(total_xp)
    check_achievements()

    return {**result, "base_xp": base_xp, "bonus_xp": bonus, "total_xp": total_xp, "stars": stars}


def is_lesson_unlocked(section_idx: int, lesson_idx: int) -> bool:
    """Check if a lesson is available to play."""
    s = get_state()
    if section_idx == 0 and lesson_idx == 0:
        return True
    # Previous lesson must be completed
    if lesson_idx > 0:
        prev_key = f"{section_idx}_{lesson_idx - 1}"
        return prev_key in s["lessons_completed"]
    else:
        # First lesson of a section: last lesson of previous section must be complete
        prev_key = f"{section_idx - 1}_3"  # 4 lessons per section (0-3)
        return prev_key in s["lessons_completed"]


def is_lesson_completed(section_idx: int, lesson_idx: int) -> bool:
    """Check if a lesson has been completed."""
    key = f"{section_idx}_{lesson_idx}"
    return key in get_state()["lessons_completed"]


def get_lesson_stars(section_idx: int, lesson_idx: int) -> int:
    """Get stars earned for a lesson (0 if not completed)."""
    key = f"{section_idx}_{lesson_idx}"
    return get_state()["lessons_completed"].get(key, 0)


# ─── ACHIEVEMENTS ────────────────────────────────────────────────
ACHIEVEMENTS = [
    {"id": "first_lesson",    "name": "Primer Paso",          "emoji": "👣", "desc": "Completa tu primera lección"},
    {"id": "section_1",       "name": "Aprendiz del Cacao",   "emoji": "🍫", "desc": "Completa la Sección 1"},
    {"id": "section_2",       "name": "Fermentador",          "emoji": "🧪", "desc": "Completa la Sección 2"},
    {"id": "section_3",       "name": "Maestro Tostador",     "emoji": "🔥", "desc": "Completa la Sección 3"},
    {"id": "section_4",       "name": "Alquimista del Temple","emoji": "⚗️", "desc": "Completa la Sección 4"},
    {"id": "section_5",       "name": "Artista del Moldeo",   "emoji": "🎨", "desc": "Completa la Sección 5"},
    {"id": "section_6",       "name": "Sommelier del Cacao",  "emoji": "🍷", "desc": "Completa la Sección 6"},
    {"id": "all_sections",    "name": "Maestro Chocolatero",  "emoji": "🏆", "desc": "Completa todas las secciones"},
    {"id": "streak_3",        "name": "Constancia",           "emoji": "🔥", "desc": "Racha de 3 días"},
    {"id": "streak_7",        "name": "Fuego Constante",      "emoji": "🔥", "desc": "Racha de 7 días"},
    {"id": "streak_30",       "name": "Llama Eterna",         "emoji": "🌋", "desc": "Racha de 30 días"},
    {"id": "perfect_lesson",  "name": "Perfección",           "emoji": "⭐", "desc": "3 estrellas en una lección"},
    {"id": "xp_1000",         "name": "Explorador",           "emoji": "🗺️", "desc": "Acumula 1,000 XP"},
    {"id": "xp_5000",         "name": "Experto",              "emoji": "💎", "desc": "Acumula 5,000 XP"},
    {"id": "lessons_10",      "name": "Dedicación",           "emoji": "📚", "desc": "Completa 10 lecciones"},
]


def check_achievements():
    """Check and unlock any new achievements."""
    s = get_state()
    unlocked = s["achievements"]
    completed = s["lessons_completed"]

    def unlock(aid):
        if aid not in unlocked:
            unlocked.append(aid)

    # First lesson
    if len(completed) >= 1:
        unlock("first_lesson")

    # Sections (4 lessons each, indices 0-3)
    for sec_idx in range(6):
        section_complete = all(f"{sec_idx}_{l}" in completed for l in range(4))
        if section_complete:
            unlock(f"section_{sec_idx + 1}")

    # All sections
    all_done = all(f"{s}_{l}" in completed for s in range(6) for l in range(4))
    if all_done:
        unlock("all_sections")

    # Streaks
    if s["streak"] >= 3:
        unlock("streak_3")
    if s["streak"] >= 7:
        unlock("streak_7")
    if s["streak"] >= 30:
        unlock("streak_30")

    # Perfect lesson
    if any(stars == 3 for stars in completed.values()):
        unlock("perfect_lesson")

    # XP milestones
    if s["xp"] >= 1000:
        unlock("xp_1000")
    if s["xp"] >= 5000:
        unlock("xp_5000")

    # Lessons count
    if len(completed) >= 10:
        unlock("lessons_10")

    save_state()


def reset_state():
    """Reset the entire user progress."""
    global _state
    _state = DEFAULT_STATE.copy()
    save_state()
    return _state
