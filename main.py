import speech_recognition as sr
import pyttsx3
    
def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        print(command)
        if command:
            perform_command(command)

def perform_command (command): 
    if "calender" in command:
        speak("What would you like to do with your calendar?")
    elif "goodbye" in command:
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
