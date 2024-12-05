import datetime
import os
import speech_recognition as sr
import win32com.client
import webbrowser
import google.generativeai as genai
from click import prompt
from colorama import Fore, Back, Style

from win32console import FOREGROUND_BLUE

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def chat(s):
    print("this for only chat")


def AI(prompt):

    genai.configure(api_key="AIzaSyDR8h-0OR_zgHqO_ZunKzxjV-WdRyoQHZY")
    texts =f"AI response for prompt::\n {prompt} \n**************************\n\n"

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[]
    )

    # texts += model[0]["text"]
    # f"{''.join(prompt.split('Jarvis')[1:])}"
    response = chat_session.send_message(f"{''.join(prompt.split('Jarvis')[1:])}")
    texts += response.text
    speaker.Speak("got it sir")
    print(Fore.CYAN+response.text)

    if not os.path.exists("openai"):
        os.mkdir("openai")
    with open(f"openai/{' '.join(prompt.split('Jarvis')[1:])}.txt","w")as f:
        f.write(texts)
    speaker.Speak(response.text)

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {Fore.LIGHTBLUE_EX+query}")
            return query
        except Exception as e:
            print(Fore.LIGHTGREEN_EX+"Please say something.")
            return "please say something"

speaker.Speak("I am Jarvis AI")
while True:
    print(Fore.YELLOW+"Listening...")
    s = takeCommand()
    speaker.Speak(s)

    if s == "shutdown":
        speaker.Speak("Goodbye, Sir")
        break



    filepath = [["Hitachi video", r"C:\Users\Tirth\Downloads\itachi.mp4"],
                ["vs code",r"C:\Users\Tirth\AppData\Local\Programs\Microsoft VS Code\code.exe"],
                ["my picture",r"D:\code\wallpaper\2.jpg"],
                ["camera",r"C:\Users\Tirth\Desktop\Camera.lnk"]]

    for path in filepath:
        if f"open {path[0]}".lower() in s.lower():
            speaker.Speak(f"opening {path[0]} for you sir...........")
            os.startfile(path[1])

    sites = [["youtube", "https://www.youtube.com"],
             ["github", "https://github.com"],["instagram", "https://instagram.com"],
             ["chrome browser","https://www.google.com/"],
             ["brave browser",r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"]]
    for site in sites:
        if f"open {site[0]}".lower() in s.lower():
            speaker.Speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])

    if "the time" in s.lower():
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        speaker.Speak(time)

    elif "who invented you" in s:
        print("i am invented by TIRTH SONIGARA")
        speaker.Speak(" i am invented by TIRTHSONIGARA")

    elif "hello Jarvis".lower() in s.lower():
        AI(prompt=s)




