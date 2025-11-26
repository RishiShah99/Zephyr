# Zephyr Integration Guide

## Overview
Zephyr now has **two integrated components** that work seamlessly together:

1. **Tiny Zephyr** - Small black popup box (Ctrl+Alt+Z)
2. **Zephyr Dashboard** - Full React/Electron app with advanced features

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Zephyr System                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────┐         ┌──────────────────┐     │
│  │  Tiny Zephyr    │         │  API Server      │     │
│  │  (app.py)       │◄────────┤  (Port 5000)     │     │
│  │  - Ctrl+Alt+Z   │         │  - Flask REST    │     │
│  │  - Small popup  │         │  - Bridge layer  │     │
│  │  - Quick tasks  │         └──────────────────┘     │
│  └─────────────────┘                 ▲                │
│         │                             │                │
│         │ Expand Button               │                │
│         ▼                             │                │
│  ┌─────────────────────────────────────────┐           │
│  │  Zephyr Dashboard                       │           │
│  │  (dashboard-app/)                       │           │
│  │  - React + Electron                     │───────────┘
│  │  - Full-featured UI                     │
│  │  - Memory management                    │
│  │  - Project tracking                     │
│  │  - Advanced features                    │
│  └─────────────────────────────────────────┘
│
└─────────────────────────────────────────────────────────┘
```

## How It Works

### 1. Tiny Zephyr (Small Black Box)
- **File:** `app.py`, `ui.py`
- **Trigger:** Press `Ctrl+Alt+Z` anywhere on your system
- **Features:**
  - Quick voice/text commands
  - Fast responses
  - Minimal, clean interface
  - Always accessible via hotkey
  - **NEW: Expand button** to launch full dashboard

### 2. API Server (Background Service)
- **File:** `api_server.py`
- **Port:** `http://localhost:5000`
- **Purpose:** Acts as a bridge between Tiny Zephyr and Dashboard
- **Auto-starts:** Launches automatically when you start Tiny Zephyr
- **Endpoints:**
  - `/command` - Execute Zephyr commands
  - `/memory` - Manage memory/facts
  - `/projects` - Project management
  - `/spotify/control` - Music control

### 3. Zephyr Dashboard (Full App)
- **Location:** `dashboard-app/`
- **Tech Stack:** React + Vite + Electron + TailwindCSS
- **Launch Method:** Click "⛶ Expand" button in Tiny Zephyr
- **Features:**
  - Full visual dashboard
  - Memory browser
  - Project management
  - Test zone for commands
  - Rich UI with animations

## Startup Process

When you run `app.py`:
1. ✅ Single instance check (prevents duplicates)
2. ✅ API server starts on port 5000 (background thread)
3. ✅ System tray icon appears
4. ✅ Global hotkey registered (Ctrl+Alt+Z)
5. ✅ Tiny Zephyr ready
6. ✅ Click "Expand" → Dashboard launches

## Usage Workflow

### Quick Tasks (Use Tiny Zephyr)
```
1. Press Ctrl+Alt+Z
2. Type command
3. Get instant response
4. Press Escape to hide
```

### Advanced Tasks (Use Dashboard)
```
1. Press Ctrl+Alt+Z
2. Click "⛶ Expand" button
3. Dashboard opens with full interface
4. Manage memory, projects, etc.
5. Commands sync with Tiny Zephyr via API
```

## File Organization

### Core Files (Tiny Zephyr)
- `app.py` - Main application entry point
- `ui.py` - Tkinter UI for small popup
- `assistant.py` - Command handling
- `groq_nlp.py` - AI/NLP processing
- `settings.py` - Configuration

### Backend Services
- `api_server.py` - REST API server
- `memory_db.py` - Database layer
- `projects.py` - Project management
- `weather.py` - Weather integration
- `spotify.py` - Music control

### Dashboard (React App)
```
dashboard-app/
├── src/
│   ├── components/
│   │   ├── Dashboard.jsx     # Main dashboard view
│   │   ├── Memory.jsx         # Memory management
│   │   ├── Projects.jsx       # Project tracking
│   │   ├── TestZone.jsx       # Command testing
│   │   └── ...
│   └── App.jsx                # Main React app
├── electron/
│   ├── main.js                # Electron main process
│   └── preload.js             # Electron preload
└── package.json               # Dependencies
```

## Branch Strategy (RESOLVED)

### ❌ OLD Problem
- **main branch** - Original tiny Zephyr only
- **react/zephyr-v3 branch** - Had duplicated tiny Zephyr + Dashboard

### ✅ NEW Solution (Current State)
- **zephyr-v3 branch** - Has BOTH integrated:
  - Original tiny Zephyr (enhanced with expand button)
  - Dashboard app
  - API server connecting them
- **main branch** - Kept for reference (legacy)

## Communication Flow

```
User Action → Tiny Zephyr → API Server → Backend Services
                    ↓
              Dashboard ← API Server ← Backend Services
```

**Example: Adding a memory**
1. User types in Tiny Zephyr: "remember my birthday is June 15"
2. Command sent to `assistant.py`
3. Stored in `memory_db.py`
4. Dashboard can view this via API call to `/memory`

**Example: Using Dashboard**
1. User clicks "Add Project" in Dashboard
2. Dashboard sends POST to `http://localhost:5000/projects`
3. API server calls `projects.py`
4. Project saved to database
5. Visible in both Dashboard and Tiny Zephyr

## Installation & Setup

### First Time Setup
```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Install Node.js dependencies for dashboard
cd dashboard-app
npm install
cd ..

# 3. Run Zephyr
python app.py
```

### Daily Usage
```bash
# Just run this - everything starts automatically:
python app.py

# Or double-click:
start_zephyr.bat
```

## Testing the Integration

1. **Test Tiny Zephyr:**
   - Press `Ctrl+Alt+Z`
   - Type "what's the weather in Toronto"
   - Should get response

2. **Test API Server:**
   - Visit `http://localhost:5000/health` in browser
   - Should see: `{"status": "online"}`

3. **Test Expand Button:**
   - Press `Ctrl+Alt+Z`
   - Click "⛶ Expand"
   - Dashboard should open in Electron window

4. **Test Integration:**
   - Add a memory in Tiny Zephyr: "remember my favorite color is blue"
   - Click Expand → Open Dashboard
   - Go to Memory tab
   - Should see the memory listed

## Troubleshooting

### API Server Not Starting
```python
# Check if port 5000 is available
netstat -ano | findstr :5000

# Kill any process using port 5000
taskkill /PID <process_id> /F
```

### Dashboard Won't Launch
```bash
# Ensure Node.js is installed
node --version
npm --version

# Reinstall dependencies
cd dashboard-app
npm install
```

### Expand Button Not Working
- Check console output when clicking expand
- Ensure `dashboard-app/` folder exists
- Verify npm is in system PATH

## Future Enhancements

- [ ] Make dashboard remember window position
- [ ] Add sync indicators between Tiny Zephyr and Dashboard
- [ ] Package as standalone executable
- [ ] Auto-update capability
- [ ] Cloud sync for memory/projects

## Summary

✅ **Tiny Zephyr** - Fast, always accessible (Ctrl+Alt+Z)  
✅ **Dashboard** - Rich features, launched via Expand button  
✅ **API Server** - Connects everything seamlessly  
✅ **Branches Merged** - One unified system  

You now have the best of both worlds! 🚀
