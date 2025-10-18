import threading
import time
import importlib

from ui import open_popup
from assistant import handle_command
from settings import get_hotkey, is_wake_word_enabled, load_settings


def main():
    settings = load_settings()
    enable_voice = settings.get("enable_voice", False)
    enable_gemini = settings.get("enable_gemini", True)
    
    # Create overlay with settings
    overlay = open_popup(
        on_submit=lambda text: handle_command(text, ask=_ask_via_overlay, use_gemini=enable_gemini),
        enable_voice=enable_voice
    )
    overlay.hide()  # start hidden until hotkey or wake word (we may show it below)

    # Register global hotkey to toggle overlay
    keyboard = None
    try:
        keyboard = importlib.import_module('keyboard')
    except Exception:
        keyboard = None

    hotkey = get_hotkey()
    if keyboard is not None and hotkey:
        try:
            keyboard.add_hotkey(hotkey, lambda: _toggle(overlay))
            print(f"Hotkey registered: {hotkey}")
        except Exception as e:
            print(f"Failed to register hotkey: {e}")
    else:
        print("'keyboard' module not available — global hotkey disabled. Install with 'pip install keyboard'.")

    # Start wake word listener in background
    def on_wake():
        try:
            overlay.show()
        except Exception as e:
            print(f"Overlay show failed: {e}")

    started_wake = False
    if is_wake_word_enabled():
        try:
            # Lazy import to avoid hard dependency when ACCESS_KEY or modules are missing
            from wake_word_listener import listen_for_wake_word  # noqa: WPS433
            listen_for_wake_word(callback=on_wake, background=True)
            started_wake = True
        except Exception as e:
            print(f"Wake word disabled: {e}")

    # If neither hotkey nor wake-word is active, show the overlay now
    if keyboard is None and not started_wake:
        print("Showing Zephyr overlay — no hotkey/wake-word configured.")
        overlay.show()

    # Enter UI loop (blocking)
    overlay.loop()


def _toggle(overlay):
    try:
        # Tk doesn't expose visibility directly; try toggling via state
        overlay.show()
    except Exception:
        pass


def _ask_via_overlay(prompt: str) -> str:
    # Ask a follow-up question via the overlay and block until user provides input
    # For simplicity, we display the prompt and wait for the next entry submit.
    result_container = {'value': None}

    ov = open_popup()
    ov.response.configure(text=prompt)

    def on_submit(text: str):
        result_container['value'] = text
        return ""  # don't speak while asking

    # Temporarily override submit handler
    old = ov.on_submit
    ov.on_submit = on_submit

    # Poll until value is set; keep UI responsive
    while result_container['value'] is None:
        ov.root.update()
        time.sleep(0.05)

    # Restore
    ov.on_submit = old
    return result_container['value']


if __name__ == "__main__":
    main()
