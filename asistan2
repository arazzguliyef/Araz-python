import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language= "tr=TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak('Sistem çalışmıyor')
        return voice
def response(voice):
    if "nasılsın" in voice:
        speak("Şükürler olsun,sen nasılsın?")
    if "Hayır" in voice:
        speak("yardım edemeyeceğim için özür dilerim.")
    elif "adın ne" in voice:
        speak("Benim adım Nuray.")
    elif 'duyuyormusun' in voice:
        speak("Evet konuş")
    elif "bişey sora bilirmiyim" in voice:
        speak("Seni dinliyorum")
    elif "Saat" in voice:
        speak(datetime.now().srtftime("%H:%M:%S"))
    elif "Arama yap" in voice:
        search = record("Ne aramak istiyorsun?")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak(search + "için bulduklarım")
    if "tamamdır" in voice:
        speak("Görüşürüz")
        exit()
        

def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("Merhaba Araz, İstediyin birşey varmi?.")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
