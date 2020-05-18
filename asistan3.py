import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
from random import choice
import os
r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language= "tr=tr")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak('Sistem çalışmıyor')
        return voice
def response(voice):
    if "Hayır" in voice:
        speak("yardım edemeyeceğim için özür dilerim.")
    if "harikasin" in voice:
        speak ("Bunu senden duymak hoştu açıkcası")
    elif "bir" in voice:
        speak("Benim adım Nuray.")
    elif 'duyuyormusun' in voice:
        speak("Evet konuş")
    elif "bişey sora bilirmiyim" in voice:
        speak("Seni dinliyorum")
    elif "Saat kaç" in voice:
        speak(datetime.now().srtftime("%H:%M:%S"))
    elif "arama yap " in voice:
        search = record("Ne aramak istiyorsun?")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak(search + "için bulduklarım")
    if "tamamdır" in voice:
        speak("Görüşürüz")
        exit()

def __init__(self, gelenSes):
     self.ses = gelenSes.upper()
     self.sesBloklari = self.ses.splint()
     print(self.sesBloklari)
     self.komutlar = ["NABER",'NASILSIN','KAPAT']
        
def sohbet(self):
    sozler = ["Iyiyim sen nasılsın","Seni sormalı",
            "Benim duygularım yok,fakat seninle konuşmak iyi geliyor",
            "Araşdırdım ve buldum ki sen benim herşeyimsin."]
    secim = choice(sozler)

    self.seslendirme(secim)

def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("Yardım ede bileceyim bir şey varmı.")
time.sleep(2)
while 2:
    voice = record()
    print(voice)
    response(voice)
