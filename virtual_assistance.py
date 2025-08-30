import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice (depends on system)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-in')
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            speak("Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("Network error.")
            speak("There seems to be a network error.")
            return ""

# Example main loop
if __name__ == "__main__":
    speak("Hello, how can I help you?")
    while True:
        command = listen()
        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
