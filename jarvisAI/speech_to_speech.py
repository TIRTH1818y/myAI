import os
import datetime
import speech_recognition as sr
import win32com.client
import webbrowser
from speech_recognition import Microphone

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "please say some things"


speaker.Speak("i am jarvis AI")
while True:
    print("Lestening......")
    s = takeCommand()
    if s == "shutdown":
        speaker.Speak("Goodbye, Sir. i shut down my system.")
        break
    speaker.Speak(s)


    filepath = r"C:\Users\Tirth\Downloads\itachi.mp4"
    if f"open Hitachi video".lower() in s.lower():
        speaker.Speak(f"opening video for you sir...........")
        os.startfile(filepath)

    sites = [["youtube","https://www.youtube.com"],["github","https://github.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in s.lower():
            speaker.Speak(f"opening {site[0]} sir...........")
            webbrowser.open(site[1])









