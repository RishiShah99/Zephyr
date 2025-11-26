# 🌙 Zephyr Dashboard - Electron + React

**Beautiful, modern dashboard for Zephyr AI Assistant**

Inspired by Intel Arc's stunning blue/purple gradient aesthetic with animated glowing moon.

---

## ✨ Features

### 🎨 **Design**
- **Intel Arc-inspired** blue → purple gradient background
- **Animated glowing moon** with orbital shine effect (top-right)
- **Glass-morphism UI** with backdrop blur
- **Hover animations** - cards enlarge on hover
- **Smooth page transitions** with Framer Motion
- **Custom scrollbars** with purple accents

### 🚀 **Tech Stack**
- **Electron** - Desktop app framework
- **React** - UI library
- **Vite** - Fast build tool
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Smooth animations
- **Lucide React** - Beautiful icons

### 👻 **Screen Capture Invisibility**
- **Invisible to screen sharing** (OBS, Zoom, Teams)
- Perfect for interviews, demos, presentations
- Same tech as Quick Mode (Tkinter)

---

## 📦 Installation

```bash
# Navigate to dashboard folder
cd dashboard-app

# Install dependencies
npm install

# Start development server
npm run dev
```

This will:
1. Start Vite dev server on `http://localhost:5173`
2. Launch Electron app automatically
3. Enable hot-reload for instant changes

---

## 🎯 Pages

### 1. **Dashboard** (Home)
- Welcome section
- 8 feature cards with hover effects
- Quick stats (commands, facts, projects)

### 2. **Memory** 
- View all stored facts
- Beautiful card layout
- Timestamps for each fact

### 3. **Projects**
- Project ideas list
- Tech stack badges
- Status indicators
- Folder paths

### 4. **Test Zone**
- Live command testing
- Terminal-style output
- Quick test buttons
- Real-time responses

---

## 🎨 Design Details

### **Color Palette**
```css
Background: linear-gradient(135deg, #1e1b4b → #312e81 → #4c1d95)
Accent: #8b5cf6 (Purple)
Secondary: #3b82f6 (Blue)
Glass: rgba(255, 255, 255, 0.03) + blur(20px)
```

### **Animated Moon**
- Orbital shine rotates 360° every 2 seconds
- Soft glow pulse (3s cycle)
- Gradient from white → purple
- Position: Top-right corner

### **Hover Effects**
- Cards scale to 1.05x
- Spring animation (stiffness: 300)
- Gradient background fade-in
- Glow effect around edges

---

## 🔌 Connecting to Python Backend

The dashboard communicates with Zephyr's Python backend via HTTP API:

```javascript
// In components:
const response = await window.zephyrAPI.sendCommand('tell me a joke');
const memory = await window.zephyrAPI.getMemory();
const projects = await window.zephyrAPI.getProjects();
```

**Next Steps:**
1. Create Python API server (Flask/FastAPI)
2. Endpoints: `/command`, `/memory`, `/projects`
3. Update preload.js with correct URL

---

## 🚀 Building for Production

```bash
# Build React app
npm run build

# Package Electron app
npm run package  # (coming soon)
```

---

## 📁 Project Structure

```
dashboard-app/
├── electron/
│   ├── main.js          # Electron main process
│   └── preload.js       # Bridge to renderer
├── src/
│   ├── components/
│   │   ├── Header.jsx        # Title bar + moon
│   │   ├── Sidebar.jsx       # Navigation
│   │   ├── Dashboard.jsx     # Home page
│   │   ├── FeatureCard.jsx   # Hover cards
│   │   ├── Memory.jsx        # Facts viewer
│   │   ├── Projects.jsx      # Ideas manager
│   │   └── TestZone.jsx      # Live testing
│   ├── App.jsx          # Main app component
│   ├── main.jsx         # React entry point
│   └── index.css        # Global styles
├── index.html           # HTML template
├── package.json         # Dependencies
├── vite.config.js       # Vite configuration
└── tailwind.config.js   # Tailwind customization
```

---

## 🎯 Key Components

### **Animated Moon** (Header.jsx)
```jsx
<motion.div
  animate={{ rotate: 360 }}
  transition={{ duration: 8, repeat: Infinity }}
>
  {/* Orbital glow rotates around moon */}
</motion.div>
```

### **Hover Cards** (FeatureCard.jsx)
```jsx
<motion.div
  whileHover={{ scale: 1.05 }}
  className="glass rounded-2xl"
>
  {/* Card content */}
</motion.div>
```

### **Sidebar Navigation** (Sidebar.jsx)
```jsx
<motion.div layoutId="activeTab">
  {/* Smooth sliding indicator */}
</motion.div>
```

---

## 🎨 Customization

### **Change Colors**
Edit `tailwind.config.js`:
```javascript
colors: {
  'zephyr-purple': '#6B46C1',
  'zephyr-blue': '#4F46E5',
}
```

### **Adjust Animations**
Edit animation durations in components:
```javascript
transition={{ duration: 0.3 }}
```

### **Moon Position**
Change moon location in `Header.jsx`:
```css
className="absolute top-4 right-32"
```

---

## 🐛 Troubleshooting

**Dashboard won't start:**
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Electron window blank:**
- Check console for errors
- Verify Vite is running on port 5173
- Check `electron/main.js` loadURL path

**CSS not loading:**
```bash
# Rebuild Tailwind
npm run dev
```

---

## 🌙 **What Makes This Special**

✅ **Intel Arc aesthetic** - Premium look & feel
✅ **Animated moon** - Unique branding element  
✅ **Glass-morphism** - Modern, clean design
✅ **Hover effects** - Interactive & engaging
✅ **Screen invisible** - Perfect for demos
✅ **Fast & smooth** - 60fps animations
✅ **Beginner-friendly** - Clear UI/UX

---

## 📝 TODO

- [ ] Connect to Python backend API
- [ ] Real-time data updates
- [ ] Settings page
- [ ] Keyboard shortcuts
- [ ] Window resize animations
- [ ] Tray menu integration

---

## 🎉 Credits

**Design Inspiration:** Intel Arc Control Panel
**Built by:** Rishi
**Made with:** 🌙 and lots of coffee

---

**Ready to test?**
```bash
cd dashboard-app
npm install
npm run dev
```

Enjoy the beautiful UI! 🚀
