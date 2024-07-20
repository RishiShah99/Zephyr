import speech_recognition as sr
import pyttsx3
from planner import create_event, see_future_events
from nlp import parse_command, extract_details

def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        print(command)
        if command:
            perform_command(command)

def perform_command (command): 
    parsedcommand = parse_command(command)
    if parsedcommand == "calendar":
        speak("What would you like to do with your calendar?")
        action = listen()
        if action:
            action_details = extract_details(action)
            if "create" in action_details:
                speak("What is the name of the event?")
                name = listen()
                if name:
                    create_event(name)
                    speak(f"Event {name} has been created.")
            elif "events" in action_details:
                events = see_future_events()
                speak(events)

    elif parsedcommand == "exit":
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except Exception as e:
            print(e)
            speak("Sorry, I didn't catch that.")
            return None

def speak(text):
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
