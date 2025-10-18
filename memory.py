from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
MEM_PATH = DATA_DIR / "memory.json"


def _load() -> List[Dict]:
    if MEM_PATH.exists():
        try:
            return json.loads(MEM_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def _save(items: List[Dict]) -> None:
    MEM_PATH.write_text(json.dumps(items, indent=2), encoding="utf-8")


def remember(text: str) -> str:
    items = _load()
    items.append({
        "date": datetime.utcnow().isoformat() + "Z",
        "text": text,
    })
    _save(items)
    return "Got it. I'll remember that."


def recall(query: str) -> str:
    items = _load()[::-1]  # search most recent first
    query = query.lower()
    matches = [f"[{i['date']}] {i['text']}" for i in items if any(w in i.get('text', '').lower() for w in query.split())]
    if not matches:
        return "I couldn't find anything."
    return "Here’s what I found:\n" + "\n".join(matches[:5])
