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
        
        # Holographic transparent background
        self.root.configure(bg="#000814")
        self.root.attributes("-alpha", 0.95)  # Slight transparency for hologram effect
        
        # Position bottom-right - BIGGER for scrolling
        self.root.update_idletasks()
        self.width = 650
        self.height = 480
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        self.target_x = screen_w - self.width - 20
        self.target_y = screen_h - self.height - 50
        
        # Start position (offscreen to the right for slide-in)
        self.start_x = screen_w
        self.start_y = self.target_y
        self.root.geometry(f"{self.width}x{self.height}+{self.start_x}+{self.start_y}")
        
        # Outer glow container (holographic border)
        self.frame = tk.Frame(self.root, bg="#00F0FF", highlightthickness=0)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
        
        # Inner frame with holographic dark background
        self.inner_frame = tk.Frame(self.frame, bg="#001D3D")
        self.inner_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # HOLOGRAPHIC HEAD at top
        head_frame = tk.Frame(self.inner_frame, bg="#001D3D")
        head_frame.pack(fill=tk.X, pady=(15, 5))
        
        # Zephyr hologram avatar
        self.avatar = tk.Label(
            head_frame,
            text="◉",  # Simple circle for holographic head
            font=("Segoe UI", 72, "bold"),
            bg="#001D3D",
            fg="#00F0FF"
        )
        self.avatar.pack()
        
        # Assistant name
        self.label = tk.Label(
            head_frame,
            text="ZEPHYR",
            fg="#00F0FF",
            bg="#001D3D",
            font=("Segoe UI", 16, "bold"),
            anchor="center"
        )
        self.label.pack(pady=(5, 0))
        
        # Holographic divider
        divider = tk.Frame(self.inner_frame, bg="#00F0FF", height=1)
        divider.pack(fill=tk.X, padx=30, pady=10)
        
        # Modern entry with holographic glow
        entry_container = tk.Frame(self.inner_frame, bg="#00F0FF", highlightthickness=0)
        entry_container.pack(fill=tk.X, padx=25, pady=(0, 15))
        
        self.entry = tk.Entry(
            entry_container,
            bg="#002855",
            fg="#FFFFFF",
            insertbackground="#00F0FF",
            font=("Segoe UI", 12),
            relief=tk.FLAT,
            borderwidth=0
        )
        self.entry.pack(fill=tk.X, padx=2, pady=2, ipady=6)
        self.entry.focus_set()
        self.entry.bind("<Return>", self._submit)
        
        # Response area with SCROLLING - holographic theme
        response_container = tk.Frame(self.inner_frame, bg="#001D3D")
        response_container.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 20))
        
        self.response = scrolledtext.ScrolledText(
            response_container,
            bg="#000814",
            fg="#94D2FF",
            insertbackground="#00F0FF",
            font=("Segoe UI", 11),
            relief=tk.FLAT,
            borderwidth=0,
            padx=18,
            pady=18,
            wrap=tk.WORD,
            height=10,
            state=tk.DISABLED  # Read-only
        )
        self.response.pack(fill=tk.BOTH, expand=True)
        
        # Typing indicator (hidden by default)
        self.typing_indicator = tk.Label(
            response_container,
            text="◉ Processing...",
            fg="#00F0FF",
            bg="#001D3D",
            font=("Segoe UI", 10, "italic")
        )
        
        self.root.bind("<Escape>", lambda e: self.hide())
        
        # Animation state
        self.is_animating = False
        self.is_visible = False
        self.glow_animation_running = False
        self.typing_job = None  # Track typing animation job
        self.thinking_job = None  # Track thinking animation job
        self.processing = False  # Track if command is being processed
        
        # Protocol for window close
        self.root.protocol("WM_DELETE_WINDOW", self.cleanup)


    def _submit(self, _):
        text = self.entry.get().strip()
        if not text:
            return
        
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.DISABLED)  # Disable while processing
        self.processing = True
        
        # Clear previous response
        self.response.config(state=tk.NORMAL)
        self.response.delete(1.0, tk.END)
        self.response.config(state=tk.DISABLED)
        
        # Cancel any pending typing animations
        if self.typing_job:
            self.root.after_cancel(self.typing_job)
            self.typing_job = None
        
        # Show typing indicator
        self.typing_indicator.pack(pady=(5, 5))
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
            
        # Hide typing indicator
        self.typing_indicator.pack_forget()
        
        # Re-enable entry (but keep processing=True until typing is done)
        self.entry.config(state=tk.NORMAL)
        self.entry.focus_set()
        
        if reply:
            # Type out the response with animation (processing flag cleared in _type_text when done)
            self._type_text(reply)
            if self.enable_voice:
                self.say(reply)
        else:
            # No reply, clear processing flag now
            self.processing = False
    
    def _type_text(self, text, index=0):
        """Animated typing effect for scrollable text widget"""
        # Check if we should still be typing (not cancelled by Escape)
        if not self.is_visible:
            return
            
        if index < len(text):
            self.response.config(state=tk.NORMAL)
            self.response.insert(tk.END, text[index])
            self.response.see(tk.END)  # Auto-scroll to bottom
            self.response.config(state=tk.DISABLED)
            # Faster typing speed (10ms per character)
            self.typing_job = self.root.after(10, lambda: self._type_text(text, index + 1))
        else:
            self.response.config(state=tk.DISABLED)
            self.typing_job = None
            self.processing = False  # Done typing, clear flag
    
    def _animate_thinking(self):
        """Animate holographic processing indicator"""
        if self.entry['state'] == tk.DISABLED and self.is_visible and self.processing:
            current = self.typing_indicator.cget("text")
            indicators = ["◉ Processing...", "◎ Processing...", "○ Processing...", "◎ Processing..."]
            try:
                idx = indicators.index(current)
                next_idx = (idx + 1) % len(indicators)
            except ValueError:
                next_idx = 0
            self.typing_indicator.config(text=indicators[next_idx])
            self.thinking_job = self.root.after(300, self._animate_thinking)
        else:
            self.thinking_job = None

    def show(self):
        """Slide in from right with smooth animation"""
        if self.is_visible or self.is_animating:
            return
        
        self.is_animating = True
        self.is_visible = True
        self.root.deiconify()
        self.root.attributes("-alpha", 0.0)  # Start transparent
        
        # Sparkle animation
        self._sparkle_animation()
        
        # Start glow pulse animation
        self.glow_animation_running = True
        self._glow_pulse()
        
        # Slide and fade in
        self._slide_in()
    
    def _glow_pulse(self, step=0):
        """Continuous holographic pulsing glow effect"""
        if not self.glow_animation_running:
            return
        
        # Cycle through holographic cyan/blue variations
        colors = ["#00F0FF", "#00D4FF", "#00B8FF", "#00D4FF", "#00F0FF", "#0AF8FF"]
        color = colors[step % len(colors)]
        self.frame.configure(bg=color)
        
        # Pulse the avatar hologram too
        avatar_colors = ["#00F0FF", "#00D4FF", "#00C8FF", "#00D4FF", "#00F0FF", "#12FFFF"]
        self.avatar.configure(fg=avatar_colors[step % len(avatar_colors)])
        
        self.root.after(140, lambda: self._glow_pulse(step + 1))
    
    def _slide_in(self, step=0):
        """Smooth slide-in animation from right"""
        steps = 20
        if step <= steps:
            # Easing function (ease-out cubic)
            progress = step / steps
            eased = 1 - pow(1 - progress, 3)
            
            # Calculate position
            current_x = int(self.start_x + (self.target_x - self.start_x) * eased)
            self.root.geometry(f"{self.width}x{self.height}+{current_x}+{self.target_y}")
            
            # Fade in to 95% for holographic transparency
            alpha = eased * 0.95
            self.root.attributes("-alpha", alpha)
            
            # Continue animation
            self.root.after(16, lambda: self._slide_in(step + 1))  # ~60 FPS
        else:
            self.is_animating = False
            self.entry.focus_set()
    
    def _sparkle_animation(self, count=0):
        """Holographic avatar pulse animation"""
        if count < 10:
            # Pulse the holographic head
            sizes = [72, 74, 76, 78, 76, 74, 72, 70, 68, 70]
            self.avatar.config(font=("Segoe UI", sizes[count], "bold"))
            self.root.after(90, lambda: self._sparkle_animation(count + 1))
        else:
            self.avatar.config(font=("Segoe UI", 72, "bold"))

    def hide(self):
        """Slide out to right with smooth animation and reset state"""
        if not self.is_visible or self.is_animating:
            return
        
        self.is_animating = True
        self.is_visible = False  # Mark as hidden immediately to stop any running operations
        self.processing = False  # Cancel any processing
        self.glow_animation_running = False  # Stop glow animation
        
        # Cancel any pending animations
        if self.typing_job:
            self.root.after_cancel(self.typing_job)
            self.typing_job = None
        if self.thinking_job:
            self.root.after_cancel(self.thinking_job)
            self.thinking_job = None
        
        # Hide typing indicator
        self.typing_indicator.pack_forget()
        
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
        """Smooth slide-out animation to right"""
        steps = 15
        if step <= steps:
            # Easing function (ease-in cubic)
            progress = step / steps
            eased = pow(progress, 3)
            
            # Calculate position
            current_x = int(self.target_x + (self.start_x - self.target_x) * eased)
            self.root.geometry(f"{self.width}x{self.height}+{current_x}+{self.target_y}")
            
            # Fade out
            alpha = 0.97 * (1 - eased)
            self.root.attributes("-alpha", alpha)
            
            # Continue animation
            self.root.after(16, lambda: self._slide_out(step + 1))
        else:
            self.root.withdraw()
            self.is_animating = False
            # is_visible already set to False in hide()

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
