import tkinter as tk
from tkinter import scrolledtext
import threading
import time


class Overlay:
    def __init__(self, on_submit=None, enable_voice=False):
        self.on_submit = on_submit
        self.enable_voice = enable_voice
        
        # Destroy any existing tk windows to prevent multiple instances
        try:
            for widget in tk._default_root.winfo_children() if tk._default_root else []:
                widget.destroy()
        except:
            pass
        
        self.root = tk.Tk()
        self.root.title("Zephyr")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 0.0)  # Start invisible
        
        # Ultra-clean minimal theme (Copilot-inspired)
        BG_DARK = "#1A1A1A"          
        BG_CARD = "#252526"          
        BG_INPUT = "#2A2A2A"         
        ACCENT_PRIMARY = "#0E639C"   
        ACCENT_BORDER = "#3A3A3A"    
        TEXT_PRIMARY = "#CCCCCC"     
        TEXT_SECONDARY = "#666666"   
        
        self.root.configure(bg=BG_DARK)
        
        # Even more compact!
        self.root.update_idletasks()
        self.width = 380
        self.height = 200  # Start very small
        self.max_height = 500  # Maximum when response is large
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        self.target_x = screen_w - self.width - 30
        self.target_y = screen_h - self.height - 70
        
        self.start_x = self.target_x
        self.start_y = screen_h
        self.root.geometry(f"{self.width}x{self.height}+{self.start_x}+{self.start_y}")
        
        # Subtle border - minimal like Copilot
        self.border_frame = tk.Frame(self.root, bg=ACCENT_BORDER, highlightthickness=0)
        self.border_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Main container
        self.main_container = tk.Frame(self.border_frame, bg=BG_DARK)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Minimal header - compact and clean
        header_frame = tk.Frame(self.main_container, bg=BG_DARK)
        header_frame.pack(fill=tk.X, padx=14, pady=(10, 6))
        
        title_label = tk.Label(
            header_frame,
            text="🌙 Zephyr", 
            fg=TEXT_PRIMARY,
            bg=BG_DARK,
            font=("Segoe UI", 10, "bold")
        )
        title_label.pack(side=tk.LEFT, anchor="w")
        
        # Expand button - launches full dashboard
        expand_btn = tk.Label(
            header_frame,
            text="⛶ Expand",
            fg=TEXT_SECONDARY,
            bg=BG_DARK,
            font=("Segoe UI", 8),
            cursor="hand2"
        )
        expand_btn.pack(side=tk.RIGHT, anchor="e", padx=(0, 10))
        expand_btn.bind("<Button-1>", lambda e: self._launch_dashboard())
        
        # Hover effect for expand button
        def expand_on_enter(e):
            expand_btn.config(fg=ACCENT_PRIMARY)
        def expand_on_leave(e):
            expand_btn.config(fg=TEXT_SECONDARY)
        expand_btn.bind("<Enter>", expand_on_enter)
        expand_btn.bind("<Leave>", expand_on_leave)
        
        # Restart button 
        restart_btn = tk.Label(
            header_frame,
            text="↻ Restart",
            fg=TEXT_SECONDARY,
            bg=BG_DARK,
            font=("Segoe UI", 8),
            cursor="hand2"
        )
        restart_btn.pack(side=tk.RIGHT, anchor="e")
        restart_btn.bind("<Button-1>", lambda e: self._restart_zephyr())
        
        # Hover effect for restart button
        def on_enter(e):
            restart_btn.config(fg=ACCENT_PRIMARY)
        def on_leave(e):
            restart_btn.config(fg=TEXT_SECONDARY)
        restart_btn.bind("<Enter>", on_enter)
        restart_btn.bind("<Leave>", on_leave)
        
        # Content area - minimal padding
        content_frame = tk.Frame(self.main_container, bg=BG_DARK)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 10))
        
        # Clean input field - right below header
        self.input_container = tk.Frame(content_frame, bg=BG_INPUT, highlightthickness=0)
        self.input_container.pack(fill=tk.X, pady=(0, 10))
        
        self.entry = tk.Entry(
            self.input_container,
            bg=BG_INPUT,
            fg=TEXT_PRIMARY,
            insertbackground=TEXT_PRIMARY,
            font=("Segoe UI", 9),
            relief=tk.FLAT,
            borderwidth=0
        )
        self.entry.pack(fill=tk.X, padx=10, pady=8)
        self.entry.bind("<Return>", self._submit)
        
        # Placeholder management
        self.placeholder_active = True
        self.entry.insert(0, "Ask anything...")
        self.entry.config(fg=TEXT_SECONDARY)
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._restore_placeholder)
        
        # Response area with auto-showing scrollbar
        self.response_frame = tk.Frame(content_frame, bg=BG_DARK)
        self.response_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar (hidden by default, only shows when needed)
        self.scrollbar = tk.Scrollbar(self.response_frame, bg=BG_DARK, troughcolor=BG_DARK, activebackground=TEXT_SECONDARY)
        
        self.response = tk.Text(
            self.response_frame,
            bg=BG_DARK,
            fg=TEXT_PRIMARY,
            font=("Segoe UI", 9),
            relief=tk.FLAT,
            borderwidth=0,
            padx=0,
            pady=0,
            wrap=tk.WORD,
            height=1,
            state=tk.DISABLED,
            highlightthickness=0,
            yscrollcommand=self._on_scroll
        )
        self.response.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure scrollbar
        self.scrollbar.config(command=self.response.yview)
        
        # Status indicator - minimal
        self.status_container = tk.Frame(self.main_container, bg=BG_DARK)
        self.status_label = tk.Label(
            self.status_container,
            text="",
            fg=TEXT_SECONDARY,
            bg=BG_DARK,
            font=("Segoe UI", 9)
        )
        
        # Store colors for animations
        self.colors = {
            'bg_dark': BG_DARK,
            'bg_card': BG_CARD,
            'bg_input': BG_INPUT,
            'accent_primary': ACCENT_PRIMARY,
            'accent_border': ACCENT_BORDER,
            'text_primary': TEXT_PRIMARY,
            'text_secondary': TEXT_SECONDARY
        }
        
        self.root.bind("<Escape>", lambda e: self.hide())
        
        # Animation state
        self.is_animating = False
        self.is_visible = False
        self.glow_animation_running = False
        self.typing_job = None  
        self.thinking_job = None  
        self.processing = False  
        
        # Protocol for window close - hide instead of quit
        self.root.protocol("WM_DELETE_WINDOW", self.hide)

    def _on_scroll(self, first, last):
        """Show/hide scrollbar based on content size"""
        first, last = float(first), float(last)
        
        # Only show scrollbar if content doesn't fit (not everything is visible)
        if first > 0.0 or last < 1.0:
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        else:
            self.scrollbar.pack_forget()
        
        # Update scrollbar
        self.scrollbar.set(first, last)

    def _clear_placeholder(self, event):
        """Clear placeholder text on focus"""
        if self.placeholder_active:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=self.colors['text_primary'])
            self.placeholder_active = False
    
    def _restore_placeholder(self, event):
        """Restore placeholder if empty"""
        if not self.entry.get():
            self.entry.insert(0, "Ask anything...")
            self.entry.config(fg=self.colors['text_secondary'])
            self.placeholder_active = True

    def _submit(self, _):
        text = self.entry.get().strip()
        if not text or self.placeholder_active:
            return
        
        # Clear input and keep dark background
        self.entry.delete(0, tk.END)
        self.placeholder_active = False
        self.entry.config(state=tk.DISABLED, disabledforeground=self.colors['text_secondary'], disabledbackground=self.colors['bg_input'])
        self.processing = True
        
        # Clear previous response
        self.response.config(state=tk.NORMAL)
        self.response.delete(1.0, tk.END)
        self.response.config(state=tk.DISABLED)
        
        # Cancel any pending typing animations
        if self.typing_job:
            self.root.after_cancel(self.typing_job)
            self.typing_job = None
        
        # Show sleek processing status
        self.status_container.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=(0, 16))
        self.status_label.config(text="")
        self.status_label.pack()
        self._animate_thinking()
        
        if self.on_submit:
            # Process in thread to keep UI responsive
            def _process():
                try:
                    reply = self.on_submit(text)
                    # Schedule UI update in main thread
                    if self.processing:  # Only if not cancelled
                        self.root.after(0, lambda r=reply: self._show_response(r))
                except Exception as ex:
                    if self.processing:  # Only if not cancelled
                        self.root.after(0, lambda err=str(ex): self._show_response(f"Error: {err}"))
            
            threading.Thread(target=_process, daemon=True).start()
    
    def _show_response(self, reply):
        # Only show response if we're still visible and processing (not cancelled by Escape)
        if not self.is_visible or not self.processing:
            return
            
        # Hide status
        self.status_label.pack_forget()
        
        # Re-enable entry with placeholder ready
        self.entry.config(state=tk.NORMAL, bg=self.colors['bg_input'], fg=self.colors['text_primary'])
        self.entry.focus_set()
        
        if reply:
            # Type out the response with animation
            self._type_text(reply)
            if self.enable_voice:
                self.say(reply)
        else:
            # No reply, clear processing flag now
            self.processing = False
    
    def _type_text(self, text, index=0):
        """Animated typing with auto-expanding window"""
        if not self.is_visible:
            return
            
        if index < len(text):
            self.response.config(state=tk.NORMAL)
            self.response.insert(tk.END, text[index])
            self.response.config(state=tk.DISABLED)
            
            # Auto-expand window based on content
            self._auto_resize()
            
            # Fast typing (8ms per character)
            self.typing_job = self.root.after(8, lambda: self._type_text(text, index + 1))
        else:
            self.response.config(state=tk.DISABLED)
            self.typing_job = None
            self.processing = False
    
    def _auto_resize(self):
        """Dynamically resize window based on content"""
        # Calculate required height for text
        self.response.update_idletasks()
        line_count = int(self.response.index('end-1c').split('.')[0])
        
        # Calculate new height (line_height * lines + padding)
        line_height = 20
        content_height = min(line_count * line_height, 300)  # Max 300px for response
        new_height = min(self.height + content_height - 100, self.max_height)
        
        # Smoothly resize if needed
        if new_height > self.height:
            self.height = new_height
            new_y = self.root.winfo_screenheight() - self.height - 70
            self.root.geometry(f"{self.width}x{self.height}+{self.target_x}+{new_y}")
    
    def _animate_thinking(self):
        """Smooth, modern processing animation"""
        if self.entry['state'] == tk.DISABLED and self.is_visible and self.processing:
            current = self.status_label.cget("text")
            # Sleek loading animation
            indicators = [
                "⚡ Thinking",
                "⚡ Thinking ·",
                "⚡ Thinking · ·",
                "⚡ Thinking · · ·",
                "⚡ Thinking · ·",
                "⚡ Thinking ·"
            ]
            try:
                idx = indicators.index(current)
                next_idx = (idx + 1) % len(indicators)
            except ValueError:
                next_idx = 0
            self.status_label.config(text=indicators[next_idx])
            self.thinking_job = self.root.after(180, self._animate_thinking)  # Smoother, faster
        else:
            self.thinking_job = None

    def show(self):
        """Clean slide-in animation"""
        if self.is_visible or self.is_animating:
            return
        
        self.is_animating = True
        self.is_visible = True
        
        # Reset to default small size
        self.height = 200
        
        self.root.deiconify()
        self.root.attributes("-alpha", 0.0)
        
        # Simple slide in
        self._slide_in()
    
    def _slide_in(self, step=0):
        """Smooth, minimal slide-up"""
        steps = 20
        if step <= steps:
            # Smooth ease-out
            progress = step / steps
            eased = 1 - pow(1 - progress, 3)
            
            # Slide up
            current_y = int(self.start_y + (self.target_y - self.start_y) * eased)
            self.root.geometry(f"{self.width}x{self.height}+{self.target_x}+{current_y}")
            
            # Fade in smoothly
            alpha = min(0.97, eased * 0.97)
            self.root.attributes("-alpha", alpha)
            
            self.root.after(10, lambda: self._slide_in(step + 1))
        else:
            self.is_animating = False
            self.entry.focus_set()
    
    def hide(self):
        """Slide out to right with smooth animation and reset state"""
        if not self.is_visible or self.is_animating:
            return
        
        self.is_animating = True
        self.is_visible = False  
        self.processing = False  
        self.glow_animation_running = False  
        
        # Cancel any pending animations
        if self.typing_job:
            self.root.after_cancel(self.typing_job)
            self.typing_job = None
        if self.thinking_job:
            self.root.after_cancel(self.thinking_job)
            self.thinking_job = None
        
        # Hide status label
        self.status_label.pack_forget()
        
        # Re-enable entry and clear it
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        
        # Clear response
        self.response.config(state=tk.NORMAL)
        self.response.delete(1.0, tk.END)
        self.response.config(state=tk.DISABLED)
        
        self._slide_out()
    
    def cleanup(self):
        """Complete cleanup of overlay"""
        self.processing = False
        self.is_visible = False
        self.glow_animation_running = False
        
        # Cancel all animations
        if self.typing_job:
            self.root.after_cancel(self.typing_job)
        if self.thinking_job:
            self.root.after_cancel(self.thinking_job)
        
        try:
            self.root.quit()
            self.root.destroy()
        except:
            pass
    
    def _slide_out(self, step=0):
        """Clean slide-down"""
        steps = 15
        if step <= steps:
            progress = step / steps
            eased = pow(progress, 2)
            
            current_y = int(self.target_y + (self.start_y - self.target_y) * eased)
            self.root.geometry(f"{self.width}x{self.height}+{self.target_x}+{current_y}")
            
            alpha = 0.97 * (1 - eased)
            self.root.attributes("-alpha", alpha)
            
            self.root.after(10, lambda: self._slide_out(step + 1))
        else:
            self.root.withdraw()
            self.is_animating = False
    
    def _launch_dashboard(self):
        """Launch the full Zephyr dashboard app"""
        import os
        import subprocess
        import threading
        
        def launch():
            try:
                dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard-app")
                
                # Check if dashboard exists
                if not os.path.exists(dashboard_path):
                    print(f" Dashboard app not found at: {dashboard_path}")
                    return
                
                print(f"Dashboard path: {dashboard_path}")
                
                # Check if npm is installed
                try:
                    result = subprocess.run(["npm", "--version"], capture_output=True, check=True, shell=True)
                    npm_version = result.stdout.decode().strip()
                    print(f"npm version: {npm_version}")
                except Exception as npm_error:
                    print(f" npm not found: {npm_error}")
                    return
                
                # Check if node_modules exists
                node_modules_path = os.path.join(dashboard_path, "node_modules")
                if not os.path.exists(node_modules_path):
                    print(f" Dependencies not installed. Run: cd dashboard-app && npm install")
                    return
                
                print("Launching Zephyr Dashboard...")
                
                # Launch the dashboard silently without console windows
                if os.name == 'nt':
                    # Windows: hide the console window
                    CREATE_NO_WINDOW = 0x08000000
                    subprocess.Popen(
                        ["npm", "run", "dev"],
                        cwd=dashboard_path,
                        shell=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        creationflags=CREATE_NO_WINDOW
                    )
                else:
                    # Unix-like systems
                    subprocess.Popen(
                        ["npm", "run", "dev"],
                        cwd=dashboard_path,
                        shell=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                
                print(" Dashboard launched!")
                
                # Hide tiny Zephyr after launching dashboard
                self.root.after(0, self.hide)
                
            except Exception as e:
                import traceback
                error_details = traceback.format_exc()
                print(f" Error launching dashboard: {e}\n{error_details}")
        
        # Launch in background thread to not block UI
        threading.Thread(target=launch, daemon=True).start()
    
    def _restart_zephyr(self):
        """Restart Zephyr - force kill and relaunch"""
        import sys
        import os
        import subprocess
        
        print("Restarting Zephyr...")
        
        # Get the path to pythonw.exe and app.py
        python_exe = sys.executable
        app_path = os.path.join(os.path.dirname(__file__), "app.py")
        
        # If we're running with python.exe, use pythonw.exe instead
        if python_exe.endswith("python.exe"):
            python_exe = python_exe.replace("python.exe", "pythonw.exe")
        
        # Launch new instance in background
        subprocess.Popen([python_exe, app_path], 
                        creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        
        # Force exit the entire Python process
        os._exit(0)

    def loop(self):
        self.root.mainloop()

    def say(self, text: str):
        # speak in a non-blocking thread
        def _s():
            try:
                pyttsx3 = __import__('pyttsx3')  # dynamic import to avoid lint error
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            except Exception:
                # Best-effort: no TTS available
                pass

        threading.Thread(target=_s, daemon=True).start()


_overlay_instance = None


def open_popup(on_submit=None, enable_voice=False):
    global _overlay_instance
    
    # Force destroy old instance if it exists
    if _overlay_instance is not None:
        try:
            _overlay_instance.root.quit()
            _overlay_instance.root.destroy()
        except:
            pass
        _overlay_instance = None
    
    # Create fresh instance
    _overlay_instance = Overlay(on_submit=on_submit, enable_voice=enable_voice)
    _overlay_instance.show()
    return _overlay_instance


def speak(text):
    # Convenience wrapper
    if _overlay_instance:
        _overlay_instance.say(text)
    else:
        try:
            pyttsx3 = __import__('pyttsx3')  # dynamic import
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
