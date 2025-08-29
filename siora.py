import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import json
import requests
from dotenv import load_dotenv
import cohere

load_dotenv()

VSCODE_PATH = os.getenv("VSCODE_PATH")
WEATHER_API = os.getenv("WEATHER_API")
CITY = os.getenv("CITY")
MUSIC_DIR_PATH = os.getenv("MUSIC_DIR_PATH")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(COHERE_API_KEY)

system_instruction = (
    "You are a helpful assistant that responds like a smart human. "
    "Your answers must be short, clear, and to the point. "
    "If humor is appropriate, use it briefly. "
    "Never explain that you're being concise. "
    "Avoid extra details unless directly asked. Use lists if needed, not paragraphs."
    "Your name is Siora and you are created by Ashmit Das."
)

chat_history = []

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 210)
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Siora, created by Ashmit Das, please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            return None
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception:
        print("Didn't catch that.")
        return None

def chat(query):
    global chat_history
    try:
        response = co.chat(
            model="command-nightly",
            message=query,
            chat_history=chat_history,
            preamble=system_instruction
        )
        chat_history.append({"role": "USER", "message": query})
        chat_history.append({"role": "CHATBOT", "message": response.text})
        return response.text
    except Exception:
        return "Sorry, I couldn't process that right now."

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand()
        if query is None or query.strip() == "":
            continue
        query = query.lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("Opening YouTube...")
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("www.google.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif "play music" in query:
            if os.path.exists(MUSIC_DIR_PATH):
                songs = os.listdir(MUSIC_DIR_PATH)
                if songs:
                    speak("Playing music...")
                    os.startfile(os.path.join(MUSIC_DIR_PATH, songs[0]))
                else:
                    speak("No music files found.")
            else:
                speak("Music directory not found.")

        elif "open code" in query:
            if os.path.exists(VSCODE_PATH):
                speak("Opening VS Code...")
                os.startfile(VSCODE_PATH)
            else:
                speak("VS Code path is invalid.")

        elif "weather" in query:
            url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API}&q={CITY}"
            r = requests.get(url)
            if r.status_code == 200:
                wdic = json.loads(r.text)
                try:
                    w = wdic["current"]["temp_c"]
                    cnd = wdic["current"]["condition"]["text"]
                    ws = wdic["current"]["wind_mph"]
                    hm = wdic["current"]["humidity"]
                    speak(f"The weather in {CITY} is {w} degrees celsius, current condition is {cnd}, wind speed is {ws} mph and humidity is {hm}.")
                except KeyError:
                    speak("Sorry, couldn't parse the weather details.")
            else:
                speak("Sorry, I couldn't fetch the weather.")

        elif "search in youtube" in query:
            search = query.replace("search in youtube", "").replace("about", "").strip()
            speak("Searching YouTube...")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

        elif "search in google" in query:
            search = query.replace("search in google", "").replace("about", "").strip()
            speak(f"Searching Google for {search}...")
            webbrowser.open(f"https://www.google.com/search?q={search}")

        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye!")
            break

        else:
            answer = chat(query)
            speak(answer)
