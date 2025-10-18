# 🔑 Zephyr API Keys Guide

This guide shows you exactly which API keys to get and how to obtain them.

## Priority: What You Need First

### ⭐ Essential (Free, No Credit Card)
These enable the core Jarvis experience:

1. **RSS News** - Already works, NO KEY NEEDED! ✅
2. **Porcupine Wake Word** - Required for "Yo Zephyr"
3. **WeatherAPI** - For weather updates

### 🎵 Nice to Have (Free Tier Available)
4. **Spotify** - Control your music
5. **Google Calendar** - Manage events
6. **NewsAPI** - Enhanced news (RSS already works)

### 🤖 Optional (Advanced)
7. **Google Gemini** - AI-powered extraction (not critical)

---

## 1. Porcupine Wake Word (FREE)
**For**: "Yo Zephyr" voice activation

### Steps:
1. Go to: https://console.picovoice.ai/
2. Sign up (free account)
3. Click "AccessKey" in the sidebar
4. Copy your access key
5. Add to `api_keys.py`:
   ```python
   ACCESS_KEY = "your_key_here"
   ```

### Also Need:
- Install: `pip install pvporcupine pyaudio`
- **PyAudio on Windows**: May need Visual C++ build tools
  - If pip fails, try: `pip install pipwin` then `pipwin install pyaudio`
  - OR download wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

**Free Tier**: Unlimited for personal use

---

## 2. WeatherAPI (FREE)
**For**: Current weather in any city

### Steps:
1. Go to: https://www.weatherapi.com/
2. Sign up (free account, no credit card)
3. Go to dashboard: https://www.weatherapi.com/my/
4. Copy your API Key
5. Add to `api_keys.py`:
   ```python
   WEATHER_API_KEY = "your_key_here"
   ```

**Free Tier**: 1 million calls/month (more than enough!)

**Test**: In Zephyr, type: `weather in Toronto`

---

## 3. Spotify (FREE)
**For**: Play/pause/skip songs, control playback

### Steps:
1. Go to: https://developer.spotify.com/dashboard
2. Log in with your Spotify account (free or premium)
3. Click "Create App"
   - App name: `Zephyr`
   - App description: `Personal AI assistant`
   - Redirect URI: `http://localhost:8888/callback`
   - Select: Web API
4. Copy your **Client ID** and **Client Secret**
5. Add to `api_keys.py`:
   ```python
   SPOTIFY_CLIENT_ID = "your_client_id_here"
   SPOTIFY_CLIENT_SECRET = "your_client_secret_here"
   SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"
   ```

**First Run**: Will open a browser for authorization, then works automatically!

**Test**: In Zephyr, type: `play song Blinding Lights`

**Note**: Spotify must be open on a device (PC, phone, etc.) to control playback

---

## 4. Google Calendar (FREE)
**For**: Create events, view schedule

### Steps (More Complex):
1. Go to: https://console.cloud.google.com/
2. Create new project: "Zephyr"
3. Enable Google Calendar API:
   - Go to: https://console.cloud.google.com/apis/library/calendar-json.googleapis.com
   - Click "Enable"
4. Create credentials:
   - Go to: https://console.cloud.google.com/apis/credentials
   - Click "Create Credentials" → "OAuth 2.0 Client ID"
   - Application type: Desktop app
   - Name: Zephyr Desktop
   - Download JSON file
5. Save JSON as `credentials.json` in the Zephyr folder
6. First run will open browser for authorization
7. Creates `token.json` automatically

**Free Tier**: Unlimited for personal use

**Test**: In Zephyr, type: `see upcoming events`

---

## 5. NewsAPI (OPTIONAL - RSS Already Works!)
**For**: Enhanced news headlines (but RSS works without this!)

### Steps:
1. Go to: https://newsapi.org/
2. Sign up (free account)
3. Copy your API key
4. Add to `api_keys.py`:
   ```python
   NEWS_API_KEY = "your_key_here"
   ```

**Free Tier**: 100 requests/day (enough for personal use)

**Note**: Zephyr uses RSS by default (unlimited, no key), so this is optional!

**Test**: In Zephyr, type: `news about Microsoft`

---

## 6. Google Gemini (OPTIONAL)
**For**: AI-powered text extraction (not critical)

### Steps:
1. Go to: https://ai.google.dev/
2. Click "Get API Key"
3. Create API key
4. Add to `api_keys.py`:
   ```python
   GEMINI_API_KEY = "your_key_here"
   ```

**Free Tier**: 60 requests/minute

**Note**: Currently only used for optional NLP enhancement. Zephyr works fine without it!

---

## Quick Setup Checklist

### Minimum Viable (15 minutes):
- [ ] Get Porcupine key (wake word)
- [ ] Get WeatherAPI key (weather)
- [ ] Copy `api_keys_example.py` to `api_keys.py`
- [ ] Fill in the 2 keys above

### Full Setup (30 minutes):
- [ ] Add Spotify credentials
- [ ] Setup Google Calendar OAuth
- [ ] (Optional) Get NewsAPI key
- [ ] (Optional) Get Gemini key

---

## Your `api_keys.py` Template

```python
# Porcupine Wake Word - https://console.picovoice.ai/
ACCESS_KEY = "your_porcupine_key_here"

# WeatherAPI - https://www.weatherapi.com/
WEATHER_API_KEY = "your_weather_key_here"

# Spotify - https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = "your_spotify_id_here"
SPOTIFY_CLIENT_SECRET = "your_spotify_secret_here"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

# NewsAPI (Optional) - https://newsapi.org/
NEWS_API_KEY = "your_news_key_here"

# Google Gemini (Optional) - https://ai.google.dev/
GEMINI_API_KEY = "your_gemini_key_here"
```

---

## What Works Without Any Keys?

**Fully Functional**:
- ✅ Projects (new project, list projects)
- ✅ Memory (remember, recall)
- ✅ RSS News (news about ...)
- ✅ Scenes (wake up, i'm home)
- ✅ Workspaces (start ... workspace)
- ✅ Global hotkey (Ctrl+Alt+Z)

**You can use Zephyr productively RIGHT NOW with just the free keys!**

---

## Troubleshooting

### "Porcupine not working"
- Make sure PyAudio is installed (can be tricky on Windows)
- Check that your mic is working
- Verify ACCESS_KEY in api_keys.py

### "Spotify says no devices"
- Open Spotify on ANY device (PC, phone, tablet)
- Start playing any song
- Then Zephyr can control it

### "Calendar won't authorize"
- Make sure you created OAuth credentials (not API key)
- Application type must be "Desktop app"
- Redirect URI not needed for desktop OAuth

### "News not working"
- RSS news should always work (no key needed)
- If using NewsAPI, check your daily limit (100/day free)

---

## Cost Breakdown (Monthly)

| Service | Free Tier | Cost if Exceeded |
|---------|-----------|------------------|
| Porcupine | Unlimited | Free for personal |
| WeatherAPI | 1M calls | $0 (you won't hit it) |
| Spotify | Unlimited | Free (just need account) |
| Google Calendar | Unlimited | Free |
| NewsAPI | 100/day | $449/mo (don't exceed!) |
| Gemini | 60/min | Free tier sufficient |
| **Total** | **$0/month** | **$0/month** |

**Zephyr is completely free to run!** 🎉

---

## Next Steps

1. Run `setup_venv.bat` to install packages
2. Get your API keys (start with Porcupine + Weather)
3. Copy `api_keys_example.py` to `api_keys.py`
4. Add your keys
5. Run: `python app.py`
6. Press `Ctrl+Alt+Z` or say "Yo Zephyr"!

Questions? Check TESTING.md for troubleshooting!
