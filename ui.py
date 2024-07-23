import tkinter as tk
from tkinter import simpledialog
import pyttsx3

def open_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    user_input = simpledialog.askstring("Zephyr", "How can I help you?")
    if user_input:
        print(f"You said: {user_input}")
        speak(user_input)
        # Here you can add further processing of the input

    root.destroy()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
