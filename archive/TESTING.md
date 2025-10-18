# Zephyr Testing Guide

## Test 1: Minimal Demo (ZERO Dependencies)
**What it tests**: Core UI, Projects, Memory without any installations

```powershell
C:\Users\shahr\AppData\Local\Programs\Python\Python313\python.exe demo_minimal.py
```

**Try these commands**:
- `help` - see available commands
- `test` - verify it's working
- `new project Portfolio Website: Next.js + Stripe` - create a project
- `new project AI Research Tool` - create another
- `list projects` - see all projects
- `remember my name is Rishi Shah` - store a memory
- `remember I'm working on CORNet-S` - store another
- `recall` - see all memories

**Expected**: Overlay window opens, all commands work, data saved to `data/` folder

---

## Test 2: Install Core Packages
**What it enables**: RSS news, TTS, global hotkey

```powershell
# Run the installer
.\install_core.bat

# OR manually:
pip install feedparser keyboard pyttsx3
```

**Expected**: All 3 packages install successfully

---

## Test 3: Run Full App (No API Keys)
**What works**: Everything except Spotify, Weather, Calendar, Wake Word

```powershell
C:\Users\shahr\AppData\Local\Programs\Python\Python313\python.exe app.py
```

**Expected**:
- Console shows: "Hotkey registered: ctrl+alt+z"
- Console shows: "Wake word disabled: ..." (expected, no API key)
- Console shows: "Showing Zephyr overlay — no hotkey/wake-word configured." OR overlay hidden

**Try hotkey**: Press `Ctrl+Alt+Z` to toggle overlay

**Try these commands**:
- `help` - see what works
- `new project Test App` - projects work
- `list projects` - see projects
- `remember my favorite IDE is VS Code` - memory works
- `recall` - see memories
- `wake up` - runs morning scene (will show errors for weather/calendar but continues)
- `i'm home` - runs evening scene
- `news about technology` - RSS news works!

**Expected**: Most features work, API-dependent features show helpful error messages

---

## Test 4: Setup API Keys (Optional)
**What it enables**: Spotify, Weather, News API, Wake Word, Calendar

1. Copy the example file:
```powershell
copy api_keys_example.py api_keys.py
```

2. Edit `api_keys.py` with your actual keys:
   - **Porcupine** (wake word): https://console.picovoice.ai/
   - **WeatherAPI**: https://www.weatherapi.com/ (free tier)
   - **NewsAPI**: https://newsapi.org/ (free tier)
   - **Spotify**: https://developer.spotify.com/dashboard
   - **Google Calendar**: Follow Google Calendar API setup
   - **Gemini**: https://ai.google.dev/ (optional)

3. Restart the app

**Try with keys**:
- `weather in Toronto` - if WEATHER_API_KEY set
- `play song Blinding Lights` - if Spotify keys set
- `create event Team Sync` - if Calendar setup
- Say "Yo Zephyr" - if Porcupine key + pyaudio installed

---

## Test 5: Scenes and Routines
**What it tests**: Scene system, daily brief

Edit `scenes.json` to customize:
```json
{
  "wake up": [
    {"say": "Good morning Rishi, ready to conquer the day?"},
    {"brief": {"city": "Toronto", "topic": "AI", "max": 3}}
  ],
  "i'm home": [
    {"say": "Welcome back! Time to unwind."},
    {"command": "play song Chill Vibes"}
  ]
}
```

**Try**: `wake up`, `i'm home`

---

## Test 6: Workspaces
**What it tests**: Launch dev environments

Edit `data/workspaces.json`:
```json
{
  "research": {
    "path": "C:\\Users\\shahr\\Documents\\Research",
    "open": [
      {"cmd": "code", "args": ["."]}
    ]
  },
  "hack49": {
    "path": "C:\\Users\\shahr\\Documents\\Hack49",
    "open": [
      {"cmd": "code", "args": ["."]},
      {"cmd": "chrome", "args": ["http://localhost:3000"]}
    ]
  }
}
```

**Try**: `start research workspace`, `start hack49 workspace`

---

## Common Issues

### Issue: "python not found"
**Fix**: Use full path:
```powershell
C:\Users\shahr\AppData\Local\Programs\Python\Python313\python.exe app.py
```

### Issue: "keyboard module not available"
**Fix**: 
```powershell
pip install keyboard
```
Then restart app

### Issue: "Wake word disabled"
**Expected** if:
- No `api_keys.py` file
- No ACCESS_KEY in api_keys.py
- No pvporcupine or pyaudio installed

**Fix**: Add Porcupine key, install: `pip install pvporcupine pyaudio`

### Issue: TTS not speaking
**Fix**: Install pyttsx3: `pip install pyttsx3`

### Issue: Hotkey not working
**Fix**: 
1. Install keyboard: `pip install keyboard`
2. Run as administrator (some systems require it)
3. Check if another app is using Ctrl+Alt+Z

### Issue: "No active Spotify devices"
**Fix**: Open Spotify on your PC or phone, start playing any song, then try again

---

## Success Checklist

- [ ] ✅ Minimal demo runs (zero dependencies)
- [ ] ✅ Core packages installed (feedparser, keyboard, pyttsx3)
- [ ] ✅ Full app launches without errors
- [ ] ✅ Hotkey toggles overlay (Ctrl+Alt+Z)
- [ ] ✅ Projects work (new project, list projects)
- [ ] ✅ Memory works (remember, recall)
- [ ] ✅ RSS news works (news about ...)
- [ ] ⏳ API keys configured (optional)
- [ ] ⏳ Spotify controls work (optional)
- [ ] ⏳ Weather works (optional)
- [ ] ⏳ Calendar works (optional)
- [ ] ⏳ Wake word works (optional)
- [ ] ⏳ Scenes customized

---

## Next: Advanced Features

Once basics work, enable:
1. **System tray** - minimize to tray, quick access
2. **Presence triggers** - auto "wake up" when you unlock PC
3. **Voice input** - mic button in overlay
4. **Templates** - scaffold new projects automatically
5. **Vector memory** - semantic recall with embeddings

Run `check_setup.py` anytime to see what's installed!
