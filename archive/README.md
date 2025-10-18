# Zephyr: Personal desktop copilot

Zephyr is a keyboard- or wake-word-activated desktop copilot. Hit a global hotkey and a small overlay pops up in the bottom-left so you can type a command, or say “Yo Zephyr” to bring it up hands‑free.

## Features
- Overlay UI (bottom-left, always on top) with global hotkey (`Ctrl+Alt+Z`)
- Wake word using Porcupine (keyword file `Yo_Zephyr.ppn`)
- Spotify controls: play/pause/skip/current song
- Calendar: create event, list upcoming events (Google Calendar)
- Weather: current weather via WeatherAPI
- News: RSS-based (no API key) with NewsAPI fallback
- Local Projects: quickly log “new project …” to `data/projects.json`

## Quick start (Windows PowerShell)

1) Install dependencies (examples):

	Optional, you may already have some packages. Install as needed.

2) Run the app:

	- Start the overlay/hotkey entrypoint:
	  `python app.py`

	- Use the hotkey `Ctrl+Alt+Z` to toggle the overlay.
	- Say “Yo Zephyr” to bring up the overlay (Porcupine access key required in `api_keys.py`).

## Configuration

`config.json` controls:
- `hotkey`: global hotkey string
- `wake_word_enabled`: whether to start the wake listener
- `offline_mode`: when true, prefer RSS news

## Notes
- Place API keys in `api_keys.py` as referenced by modules (WeatherAPI, NewsAPI, Spotify, Porcupine, Google Calendar).
- If you don’t need a service, run `app.py` directly for an interactive desktop experience.
