import speech_recognition as sr
import pyttsx3
    
def main():
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        print(command)
        # if command:
            # Perform Command

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
