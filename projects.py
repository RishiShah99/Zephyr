import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
STORE = BASE_DIR / "data"
STORE.mkdir(exist_ok=True)
PROJECTS_PATH = STORE / "projects.json"


def _load() -> list:
    if PROJECTS_PATH.exists():
        try:
            return json.loads(PROJECTS_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def _save(items: list) -> None:
    PROJECTS_PATH.write_text(json.dumps(items, indent=2), encoding="utf-8")


def create_project(name: str, description: str = "") -> dict:
    items = _load()
    item = {
        "name": name,
        "description": description,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    items.append(item)
    _save(items)
    return item


def list_projects() -> list:
    return _load()
