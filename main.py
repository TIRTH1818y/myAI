import win32com.client
import datetime
from speech_to_speech import speaker

speacker = win32com.client.Dispatch("SAPI.SpVoice")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speaker.Speak('Good Morning Sir')
    elif hour>=12 and hour<18:
        speaker.Speak('Good Afternoon sir')
    else:
        speaker.Speak('Good Evening sir')
while 1:
    print("enter text")
    s = input()
    speacker.Speak(s)
