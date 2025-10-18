import json
from pathlib import Path
from typing import Any, Dict

BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "config.json"

DEFAULTS: Dict[str, Any] = {
    "hotkey": "ctrl+alt+z",
    "wake_word_enabled": True,
    "offline_mode": True,
    "mood": {"rate": 200, "volume": 1.0},
}


def _load() -> Dict[str, Any]:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            return DEFAULTS.copy()
    return DEFAULTS.copy()


_CONFIG = _load()


def get(key: str, default: Any = None) -> Any:
    return _CONFIG.get(key, DEFAULTS.get(key, default))


def get_hotkey() -> str:
    return str(get("hotkey", DEFAULTS["hotkey"]))


def is_wake_word_enabled() -> bool:
    return bool(get("wake_word_enabled", DEFAULTS["wake_word_enabled"]))


def offline_mode() -> bool:
    return bool(get("offline_mode", DEFAULTS["offline_mode"]))


def get_mood() -> Dict[str, Any]:
    val = get("mood", DEFAULTS["mood"])
    # Ensure expected keys exist
    return {
        "rate": int(val.get("rate", DEFAULTS["mood"]["rate"])),
        "volume": float(val.get("volume", DEFAULTS["mood"]["volume"])),
    }


def load_settings() -> Dict[str, Any]:
    """Return the full config dictionary"""
    return _CONFIG.copy()
