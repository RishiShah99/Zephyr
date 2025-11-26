import threading
import time
import importlib
import sys
import os
import socket

from ui import open_popup
from assistant import handle_command
from settings import get_hotkey, is_wake_word_enabled, load_settings

# Single instance check
def ensure_single_instance():
    """Prevent multiple instances from running"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', 63742))  # Unique port for Zephyr
        return sock  # Keep socket alive to hold the lock
    except socket.error:
        print("Zephyr is already running!")
        sys.exit(0)


def start_api_server():
    """Start the API server in background for dashboard communication"""
    try:
        import api_server
        print("[OK] Starting API server for dashboard...")
        api_server.app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            threaded=True,
            use_reloader=False
        )
    except Exception as e:
        print(f"[WARNING] API server failed to start: {e}")


def main():
    # Ensure only one instance runs
    instance_lock = ensure_single_instance()
    
    # Start API server in background thread for dashboard integration
    api_thread = threading.Thread(target=start_api_server, daemon=True)
    api_thread.start()
    print("[OK] API server starting on http://localhost:5000")
    
    settings = load_settings()
    enable_voice = settings.get("enable_voice", False)
    enable_gemini = settings.get("enable_gemini", True)
    
    # Create overlay with settings
    overlay = open_popup(
        on_submit=lambda text: handle_command(text, ask=_ask_via_overlay, use_gemini=enable_gemini),
        enable_voice=enable_voice
    )
    
    # Show daily briefing on first launch
    try:
        from briefings import get_daily_briefing, should_show_morning_briefing
        if should_show_morning_briefing():
            briefing = get_daily_briefing()
            overlay.show()
            overlay._show_response(briefing)
        else:
            overlay.hide()
    except Exception as e:
        print(f"[WARNING] Briefing failed: {e}")
        overlay.hide()
    
    # Start system tray icon
    tray_icon = None
    try:
        from tray_icon import ZephyrTrayIcon
        tray_icon = ZephyrTrayIcon(overlay, lambda: _quit_app(overlay))
        tray_icon.start_in_background()
        print("[OK] System tray icon started")
    except Exception as e:
        print(f"⚠ Tray icon failed: {e}")

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
            print(f"✅ Global hotkey registered: {hotkey.upper()}")
            print(f"   Press {hotkey.upper()} anywhere on your system to open Zephyr!")
        except Exception as e:
            print(f"❌ Failed to register global hotkey: {e}")
            print(f"   On Windows, you need to run as Administrator for system-wide hotkeys.")
            print(f"   Right-click start_zephyr_admin.bat and select 'Run as administrator'")
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
        if overlay.is_visible:
            overlay.hide()
        else:
            overlay.show()
    except Exception as e:
        print(f"Toggle error: {e}")


def _quit_app(overlay):
    """Properly quit the application"""
    try:
        print("Shutting down Zephyr...")
        overlay.root.quit()
        sys.exit(0)
    except Exception as e:
        print(f"Quit error: {e}")
        sys.exit(0)


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
