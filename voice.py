import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize the speech engine and recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
    except Exception as e:
        print("Sorry, I could not recognize what you said. Please try again.")
        return ""
    return command

def play_song(song):
    talk(f"Playing {song}")
    pywhatkit.playonyt(song)

def get_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f"Current time is {current_time}")

def search_wikipedia(topic):
    info = wikipedia.summary(topic, 1)
    talk(info)

def run_assistant():
    while True:
        command = listen()
        
        if 'play' in command:
            song = command.replace('play', '')
            play_song(song)
        
        elif 'time' in command:
            get_time()

       # elif 'date' in command:
        #    get_date()

        elif 'who is' in command:
            topic = command.replace('who is', '')
            search_wikipedia(topic)

        elif 'stop' in command:
            talk("Goodbye!")
            break

if __name__ == "__main__":
    talk("Hello! How can I help you today?")
    run_assistant()
