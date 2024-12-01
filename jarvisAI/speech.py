import win32com.client

speacker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:

    print("enter text")
    s = input()
    speacker.Speak(s)