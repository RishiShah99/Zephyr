from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Dict, Any

from ui import speak
from assistant import handle_command

BASE_DIR = Path(__file__).parent
SCENES_PATH = BASE_DIR / "scenes.json"


DEFAULT_SCENES = {
    "wake up": [
        {"say": "Good morning. What would you like to work on today?"},
        {"command": "current song"},
        {"brief": {"city": "Toronto", "topic": "technology", "max": 3}},
    ],
    "i'm home": [
        {"say": "Welcome back. I've prepared your evening brief."},
        {"brief": {"city": "Toronto", "topic": "world", "max": 3}},
    ],
}


def load_scenes() -> Dict[str, Any]:
    if not SCENES_PATH.exists():
        SCENES_PATH.write_text(json.dumps(DEFAULT_SCENES, indent=2), encoding="utf-8")
    try:
        return json.loads(SCENES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return DEFAULT_SCENES


def run_scene(name: str, ask: Callable[[str], str] | None = None) -> str:
    from briefing import speak_daily_brief

    scenes = load_scenes()
    actions = scenes.get(name.lower())
    if not actions:
        return f"Scene '{name}' not found."

    outputs = []
    for step in actions:
        if "say" in step:
            speak(step["say"])  # fire and forget
            outputs.append(step["say"])
        elif "command" in step:
            outputs.append(handle_command(step["command"], ask=ask))
        elif "brief" in step:
            args = step["brief"]
            outputs.append(speak_daily_brief(args.get("city"), args.get("topic", "technology"), args.get("max", 3)))
    return "\n".join(outputs)
