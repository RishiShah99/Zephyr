"""
Minimal Zephyr Demo
Runs with zero dependencies except Python built-ins (tkinter, threading, json).
No API keys required. Tests core overlay UI and command routing.
"""
import tkinter as tk
import json
from pathlib import Path

# Minimal command handler (no external APIs)
def handle_demo_command(text):
    text = text.lower().strip()
    
    if "hello" in text or "hi" in text:
        return "Hello! I'm Zephyr. Try: 'what can you do?'"
    
    if "what can you do" in text or "help" in text:
        return """I can help with:
- Spotify (play/pause/skip) - needs spotipy
- Weather - needs weather API
- Calendar - needs Google Calendar API
- News - needs feedparser
- Projects - local storage (works now!)
- Memory - local storage (works now!)
- Scenes - routines like 'wake up'

Try: 'new project test app', 'remember my favorite color is blue', 'list projects'"""
    
    if "new project" in text:
        name = text.replace("new project", "").strip()
        if not name:
            return "What's the project name?"
        # Save to projects
        try:
            data_dir = Path(__file__).parent / "data"
            data_dir.mkdir(exist_ok=True)
            projects_file = data_dir / "projects.json"
            
            projects = []
            if projects_file.exists():
                try:
                    projects = json.loads(projects_file.read_text())
                except:
                    pass
            
            from datetime import datetime
            projects.append({
                "name": name,
                "description": "",
                "created_at": datetime.utcnow().isoformat() + "Z"
            })
            
            projects_file.write_text(json.dumps(projects, indent=2))
            return f"✓ Created project: {name}"
        except Exception as e:
            return f"Error: {e}"
    
    if "list projects" in text:
        try:
            data_dir = Path(__file__).parent / "data"
            projects_file = data_dir / "projects.json"
            
            if not projects_file.exists():
                return "No projects yet. Try: 'new project test app'"
            
            projects = json.loads(projects_file.read_text())
            if not projects:
                return "No projects yet."
            
            result = "Your projects:\n"
            for p in projects:
                result += f"• {p['name']}\n"
            return result
        except Exception as e:
            return f"Error: {e}"
    
    if "remember" in text:
        fact = text.replace("remember", "").strip()
        if not fact:
            return "What should I remember?"
        try:
            data_dir = Path(__file__).parent / "data"
            data_dir.mkdir(exist_ok=True)
            memory_file = data_dir / "memory.json"
            
            memories = []
            if memory_file.exists():
                try:
                    memories = json.loads(memory_file.read_text())
                except:
                    pass
            
            from datetime import datetime
            memories.append({
                "date": datetime.utcnow().isoformat() + "Z",
                "text": fact
            })
            
            memory_file.write_text(json.dumps(memories, indent=2))
            return "✓ Got it. I'll remember that."
        except Exception as e:
            return f"Error: {e}"
    
    if "recall" in text or "what did i" in text:
        try:
            data_dir = Path(__file__).parent / "data"
            memory_file = data_dir / "memory.json"
            
            if not memory_file.exists():
                return "I don't have any memories yet."
            
            memories = json.loads(memory_file.read_text())
            if not memories:
                return "No memories yet."
            
            result = "Here's what I remember:\n"
            for m in memories[-5:]:  # last 5
                result += f"• {m['text']}\n"
            return result
        except Exception as e:
            return f"Error: {e}"
    
    if "test" in text:
        return "✓ Zephyr is working! Core features available."
    
    return "I didn't understand that. Try 'help' to see what I can do."


class MinimalOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zephyr Demo")
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#111111")
        
        # Position bottom-left
        width = 500
        height = 300
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = 20
        y = screen_h - height - 50
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Header
        header = tk.Label(
            self.root,
            text="Zephyr - Minimal Demo (No API keys needed)",
            bg="#222222",
            fg="#00FF00",
            font=("Consolas", 10, "bold"),
            pady=8
        )
        header.pack(fill=tk.X)
        
        # Main frame
        frame = tk.Frame(self.root, bg="#111111")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Prompt
        tk.Label(
            frame,
            text="How can I help?",
            fg="#EEEEEE",
            bg="#111111",
            font=("Segoe UI", 10)
        ).pack(anchor="w")
        
        # Entry
        self.entry = tk.Entry(
            frame,
            bg="#222222",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            font=("Segoe UI", 11)
        )
        self.entry.pack(fill=tk.X, pady=(5, 0))
        self.entry.focus_set()
        self.entry.bind("<Return>", self._on_submit)
        
        # Response area
        self.response = tk.Text(
            frame,
            bg="#111111",
            fg="#CCCCCC",
            font=("Segoe UI", 9),
            wrap=tk.WORD,
            height=10,
            borderwidth=0,
            highlightthickness=0
        )
        self.response.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Instructions
        footer = tk.Label(
            self.root,
            text="Press Enter to send • ESC to quit • Try: 'help', 'new project test', 'remember my name is Rishi'",
            bg="#222222",
            fg="#888888",
            font=("Consolas", 8),
            pady=5
        )
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.root.bind("<Escape>", lambda e: self.root.quit())
        
        # Welcome message
        self.response.insert("1.0", "Welcome to Zephyr! Type 'help' to see what I can do.\n\n")
    
    def _on_submit(self, event):
        text = self.entry.get().strip()
        if not text:
            return
        
        self.entry.delete(0, tk.END)
        
        # Show user input
        self.response.insert(tk.END, f"You: {text}\n", "user")
        self.response.see(tk.END)
        
        # Get response
        try:
            reply = handle_demo_command(text)
            self.response.insert(tk.END, f"Zephyr: {reply}\n\n", "zephyr")
        except Exception as e:
            self.response.insert(tk.END, f"Error: {e}\n\n", "error")
        
        self.response.see(tk.END)
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    print("Starting Zephyr minimal demo...")
    print("This demo works with ZERO external dependencies!")
    print("=" * 60)
    overlay = MinimalOverlay()
    overlay.run()
