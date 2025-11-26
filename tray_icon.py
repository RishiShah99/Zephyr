"""
System tray icon for Zephyr
Shows status and provides quit option
"""
import pystray
from PIL import Image, ImageDraw
import threading


def create_icon_image():
    """Create a simple moon icon for the system tray"""
    # Create a dark moon icon
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (0, 0, 0, 0))
    dc = ImageDraw.Draw(image)
    
    # Draw moon shape
    dc.ellipse([8, 8, 56, 56], fill='white', outline='white')
    dc.ellipse([16, 8, 56, 56], fill='black', outline='black')
    
    return image


class ZephyrTrayIcon:
    def __init__(self, overlay, on_quit):
        self.overlay = overlay
        self.on_quit_callback = on_quit
        self.icon = None
        
    def show_window(self, icon, item):
        """Show the Zephyr window"""
        self.overlay.show()
    
    def restart_zephyr(self, icon, item):
        """Restart Zephyr"""
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
        
        # Quit current instance
        self.icon.stop()
        if self.on_quit_callback:
            self.on_quit_callback()
    
    def quit_zephyr(self, icon, item):
        """Quit Zephyr completely"""
        print("Quitting Zephyr from tray...")
        self.icon.stop()
        if self.on_quit_callback:
            self.on_quit_callback()
    
    def run(self):
        """Run the system tray icon"""
        image = create_icon_image()
        
        menu = pystray.Menu(
            pystray.MenuItem('Show Zephyr', self.show_window, default=True),
            pystray.MenuItem('Restart', self.restart_zephyr),
            pystray.MenuItem('Quit', self.quit_zephyr)
        )
        
        self.icon = pystray.Icon(
            'Zephyr',
            image,
            'Zephyr AI Assistant',
            menu
        )
        
        # Run in separate thread
        self.icon.run()
    
    def start_in_background(self):
        """Start tray icon in background thread"""
        tray_thread = threading.Thread(target=self.run, daemon=True)
        tray_thread.start()
        return tray_thread


if __name__ == "__main__":
    print("Testing tray icon...")
    
    class MockOverlay:
        def show(self):
            print("Overlay shown!")
    
    tray = ZephyrTrayIcon(MockOverlay(), lambda: print("Quit called"))
    tray.run()
