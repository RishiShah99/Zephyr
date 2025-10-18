import re
from typing import Callable, Optional

from spotify import play_song, pause_song, skip_song, get_current_song
from planner import create_event, see_future_events
from weather import get_weather

try:
    from news_rss import get_news_rss
    HAS_RSS = True
except Exception:
    HAS_RSS = False

try:
    from gemini_nlp import understand_command as gemini_understand, chat as gemini_chat
    HAS_GEMINI = True
except Exception:
    HAS_GEMINI = False


def _extract_after(command: str, keyword: str) -> Optional[str]:
    idx = command.lower().find(keyword)
    if idx == -1:
        return None
    return command[idx + len(keyword):].strip()


def handle_command(command: str, ask: Optional[Callable[[str], str]] = None, use_gemini: bool = True) -> str:
    """
    Smart command handler that uses Gemini AI for natural language understanding.
    Falls back to regex patterns if Gemini is unavailable or disabled.
    ask(prompt) can be provided to collect follow-ups (e.g., via UI) when details are missing.
    """
    if not command:
        return "I didn't catch that."

    cmd = command.lower().strip()
    
    # Try Gemini NLP first if enabled
    if use_gemini and HAS_GEMINI:
        try:
            understanding = gemini_understand(command)
            intent = understanding.get("intent", "unknown")
            entities = understanding.get("entities", {})
            natural_response = understanding.get("natural_response", False)
            
            # If it's general chat, use Gemini to respond
            if intent == "chat" or natural_response:
                return gemini_chat(command)
            
            # Execute structured commands based on intent
            if intent == "play_music":
                song = entities.get("song_name")
                if song:
                    return play_song(song)
                return "What song would you like to play?"
            
            if intent == "pause_music":
                return pause_song()
            
            if intent == "skip_music":
                return skip_song()
            
            if intent == "current_song":
                return get_current_song()
            
            if intent == "get_weather":
                location = entities.get("location")
                if location:
                    return get_weather(location)
                return "Which city's weather would you like?"
            
            if intent == "create_event":
                event_name = entities.get("event_name")
                if event_name:
                    create_event(event_name)
                    return f"Event '{event_name}' created!"
                return "What should I call this event?"
            
            if intent == "list_events":
                return see_future_events()
            
            if intent == "get_news":
                topic = entities.get("topic")
                if HAS_RSS:
                    return get_news_rss(topic or "technology", limit=5)
                return "News service unavailable."
            
            if intent == "create_project":
                name = entities.get("project_name")
                desc = entities.get("description", "")
                if name:
                    from projects import create_project
                    create_project(name, desc)
                    return f"Created project '{name}'!"
                return "What's the project name?"
            
            if intent == "list_projects":
                from projects import list_projects
                items = list_projects()
                if not items:
                    return "No projects yet. Try: 'create a project for my portfolio website'"
                return "Your Projects:\n" + "\n".join(f"• {p['name']}" + (f" — {p.get('description','')}" if p.get('description') else "") for p in items)
            
            if intent == "remember":
                fact = entities.get("fact")
                if fact:
                    from memory import remember
                    return remember(fact)
                return "What should I remember?"
            
            if intent == "recall":
                from memory import recall
                return recall(entities.get("query", ""))
            
            if intent == "start_workspace":
                workspace = entities.get("workspace_name")
                if workspace:
                    from workspace import start_workspace
                    return start_workspace(workspace)
                return "Which workspace should I start?"
            
            if intent == "run_scene":
                scene = entities.get("scene_name", "")
                from scenes import run_scene
                return run_scene(scene, ask=ask)
            
        except Exception as e:
            print(f"Gemini processing error: {e}")
            # Fall through to regex patterns
    
    # Fallback to original regex-based command parsing
    return _handle_command_regex(cmd, command, ask)


def _handle_command_regex(cmd: str, original_command: str, ask: Optional[Callable[[str], str]] = None) -> str:
    """Original regex-based command parsing as fallback"""

    # Spotify controls
    if any(w in cmd for w in ["play ", "play song", "play music"]):
        # Try to extract song name
        song = None
        m = re.search(r"play (?:song )?(.*)", cmd)
        if m and m.group(1):
            song = m.group(1).strip()
        if not song and ask:
            song = ask("What song would you like to play?")
        if song:
            return play_song(song)
        return "Please tell me the song name."
    if "pause" in cmd:
        return pause_song()
    if "skip" in cmd or "next" in cmd:
        return skip_song()
    if "current song" in cmd or "what's playing" in cmd or "whats playing" in cmd:
        return get_current_song()

    # Weather
    if "weather" in cmd:
        # Try formats like "weather in Toronto"
        m = re.search(r"weather in ([\w\s,]+)", cmd)
        location = m.group(1).strip() if m else None
        if not location and ask:
            location = ask("What city?")
        if location:
            return get_weather(location)
        return "Please tell me the location."

    # Calendar
    if "create" in cmd and "event" in cmd:
        name = _extract_after(cmd, "create event") or _extract_after(cmd, "create a new event")
        if not name and ask:
            name = ask("What's the event name?")
        if name:
            create_event(name)
            return f"Event '{name}' has been created."
        return "Please provide an event name."
    if any(w in cmd for w in ["see events", "view events", "upcoming events", "what's on my calendar", "whats on my calendar"]):
        return see_future_events()

    # News
    if "news" in cmd:
        # Extract topic
        topic = None
        m = re.search(r"news (?:about|on|regarding) ([\w\s-]+)", cmd)
        if m:
            topic = m.group(1).strip()
        if not topic and ask:
            topic = ask("What topic?")
        if not topic:
            return "What topic should I search news for?"

        if HAS_RSS:
            return get_news_rss(topic, limit=5)
        else:
            # Fall back to NewsAPI if available
            try:
                from news import get_top_news
                return get_top_news(topic)
            except Exception:
                return "News is unavailable right now."

    # Projects (local notes)
    if any(w in cmd for w in ["new project", "create project"]):
        try:
            from projects import create_project
            name = None
            desc = None
            m = re.search(r"(?:new|create) project ([\w\s-]+)(?:\:\s*(.*))?", cmd)
            if m:
                name = m.group(1).strip()
                desc = (m.group(2) or "").strip() if len(m.groups()) > 1 else None
            if not name and ask:
                name = ask("Project name?")
            if desc is None and ask:
                desc = ask("Brief description? (optional)")
            if not name:
                return "Please provide a project name."
            create_project(name, desc or "")
            return f"Created project '{name}'."
        except Exception as e:
            return f"Couldn't create project: {e}"
    if any(w in cmd for w in ["list projects", "show projects"]):
        try:
            from projects import list_projects
            items = list_projects()
            if not items:
                return "No projects yet."
            return "Projects:\n" + "\n".join(f"- {p['name']} — {p.get('description','')}" for p in items)
        except Exception as e:
            return f"Couldn't list projects: {e}"

    # Workspaces
    if cmd.startswith("start ") and "workspace" in cmd:
        try:
            from workspace import start_workspace
            m = re.search(r"start (.+?) workspace", cmd)
            name = m.group(1).strip() if m else None
            if not name and ask:
                name = ask("Which workspace?")
            if not name:
                return "Please provide a workspace name."
            return start_workspace(name)
        except Exception as e:
            return f"Couldn't start workspace: {e}"

    # Memory (stubs)
    if cmd.startswith("remember "):
        try:
            from memory import remember
            fact = cmd[len("remember "):].strip()
            return remember(fact)
        except Exception:
            return "Memory module not available yet."
    if any(w in cmd for w in ["recall", "what did i say", "what did i tell you"]):
        try:
            from memory import recall
            q = cmd
            return recall(q)
        except Exception:
            return "Memory module not available yet."

    # Scenes / routines
    if any(w in cmd for w in ["wake up", "i'm home", "im home", "good morning", "good evening"]):
        try:
            from scenes import run_scene
            scene_name = "wake up" if "wake up" in cmd or "good morning" in cmd else "i'm home" if ("i'm home" in cmd or "im home" in cmd or "good evening" in cmd) else cmd
            return run_scene(scene_name, ask=ask)
        except Exception as e:
            return f"Couldn't run scene: {e}"

    # Greeting intent
    if any(w in cmd for w in ["what should i work on", "what would you like to work on", "hello", "hi", "good morning", "good evening"]):
        if ask:
            choice = ask("What would you like to work on today?")
            if choice:
                return handle_command(choice, ask=ask)
        return "How can I help today?"

    return "I can help with Spotify, weather, calendar, news, projects, and routines. Try: 'play song Yesterday', 'weather in Toronto', 'create event Team sync', 'news about Microsoft', 'new project Portfolio site: Next.js + Stripe', or 'wake up'."
