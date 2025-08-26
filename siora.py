import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

VSCODE_PATH = os.getenv("VSCODE_PATH")
WEATHER_API = os.getenv("WEATHER_API")
CITY = os.getenv("CITY")
PYCHARM_PATH = os.getenv("PYCHARM_PATH")
MUSIC_DIR_PATH = os.getenv("MUSIC_DIR_PATH")

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am Siora, created by Ashmit Das, please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube...")
            webbrowser.open("www.youtube.com")
        
        elif "open google" in query:
            speak("opening google...")
            webbrowser.open("www.google.com")
        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
        
        elif "play music" in query:
            speak("playing music...")
            songs = os.listdir(MUSIC_DIR_PATH)
            os.startfile(os.path.join(MUSIC_DIR_PATH, songs[0]))
        
        elif "open code" in query:
            speak("opening vs code...")
            os.startfile(VSCODE_PATH)
        
        elif "open pycharm" in query:
            speak("opening pycharm...")
            os.startfile(PYCHARM_PATH)
        
        elif "weather" in query:
            url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API}&q={CITY}"
            r = requests.get(url)
            wdic = json.loads(r.text)
            w = wdic["current"]["temp_c"]
            cnd = wdic["current"]["condition"]["text"]
            ws = wdic["current"]["wind_mph"]
            hm = wdic["current"]["humidity"]
            speak(f"The weather in {CITY} is {w} degrees celsius, current condition is {cnd}, wind speed is {ws} mph and humidity is {hm}.")
        
        elif "search in youtube" in query:
            search = query.replace("search in youtube", "").strip().replace("about", "").strip()
            speak("searching your requested video in youtube...")
            yt_search = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.open(yt_search)

        elif "search in google" in query:
            search = query.replace("search in google", "").strip().replace("about", "").strip()
            speak(f"searching {search} in google...")
            g_search = f"https://www.google.com/search?q={search}"
            webbrowser.open(g_search)