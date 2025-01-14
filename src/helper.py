import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def voice_input():
    s = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('listening...')
        audio = s.listen(source)
        
    try:
        text = s.recognize_google(audio)
        print("You Said: ",text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
        

def load_llm_model(user_text):
    genai.configure(api_key = GOOGLE_API_KEY)
    
    model = genai.GenerativeModel(model_name="gemini-pro")

    response = model.generate_content(user_text)
    result = response.text
    return result

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")