from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional

from ui import speak

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
WORKSPACES_PATH = DATA_DIR / "workspaces.json"

DEFAULT_WORKSPACES = {
    "research": {
        "path": str((BASE_DIR / "..").resolve()),
        "open": [
            {"cmd": "code", "args": ["."]},
        ],
        "after": [
            {"cmd": "python", "args": ["-m", "http.server"]}
        ],
    }
}


def load_workspaces() -> Dict[str, Any]:
    if not WORKSPACES_PATH.exists():
        WORKSPACES_PATH.write_text(json.dumps(DEFAULT_WORKSPACES, indent=2), encoding="utf-8")
    try:
        return json.loads(WORKSPACES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return DEFAULT_WORKSPACES


def start_workspace(name: str) -> str:
    ws = load_workspaces().get(name.lower())
    if not ws:
        return f"Workspace '{name}' not found."

    cwd = Path(ws.get("path", BASE_DIR)).resolve()
    opened = []

    def run_step(step: Dict[str, Any]):
        cmd = step.get("cmd")
        args = step.get("args", [])
        if not cmd:
            return
        try:
            subprocess.Popen([cmd, *args], cwd=cwd)
        except Exception as e:
            opened.append(f"Failed: {cmd} ({e})")

    for step in ws.get("open", []):
        run_step(step)

    for step in ws.get("after", []):
        run_step(step)

    msg = f"Started workspace '{name}'."
    speak(msg)
    return msg
