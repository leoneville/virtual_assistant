# -*- coding: utf-8 -*-

from Chatbot import Chatbot
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

rec = sr.Recognizer()

class BotFalante(Chatbot):
    def escuta(self,frase=None):
        try:
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                fala = rec.listen(mic)
            frase = rec.recognize_google(fala,language='pt-BR')
            print(frase)
        except sr.UnknownValueError:
            return ''
        return super().escuta(frase=frase)
    
    def fala(self,frase):
        voz = gTTS(frase,lang='pt-br')
        voz.save('Audio/hello.mp3')
        playsound('Audio/hello.mp3')
        super().fala(frase)

Bot = BotFalante('@Nome do seu Bot')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'Até mais :]':
        break


