import win32com.client
import google.generativeai as genai
import speech_recognition as sr


speaker = win32com.client.Dispatch("SAPI.SpVoice")


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
  history=[

  ])

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 1
    audio = r.listen(source)
    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language="en-in")
      print(f"User said: {query}")
      return query
    except Exception as e:
      print("Please say something.")
      return "please say something"
genai.configure(api_key="AIzaSyDR8h-0OR_zgHqO_ZunKzxjV-WdRyoQHZY")

print(" i am jarvis AI")
speaker.Speak("i am jatvish AI")
while True:
    print("Listening...")
    s = takeCommand()

    if "open AI".lower() in s.lower():
      response = chat_session.send_message(f"{''.join(s.split('hello')[1:])}")
      text = response.text
      print(text)
      speaker.Speak(text)
    #
    # if s == "shutdown":
    #     speaker.Speak("Goodbye, Sir")
    #     break



