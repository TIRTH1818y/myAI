import os
import google.generativeai as genai
from click import prompt
from colorama import Fore
import AIP





def AI(data):


    print("input data",data)
    genai.configure(api_key="PAISE-BHAR-KE-LE-apiKEY")
    # texts =f"AI response for prompt::\n {prompt} \n**************************\n\n"

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

    response = chat_session.send_message(data)
    # texts += response.text

    print(Fore.CYAN+response.text)

    # if not os.path.exists("openai"):
    #     os.mkdir("openai")
    # with open(f"openai/{prompt}.txt","w")as f:
    #     f.write(texts)
    #
    return response.text



