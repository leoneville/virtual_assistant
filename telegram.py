# -*- coding: utf-8 -*-

import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("Seu token do Telegram")
bot = Chatbot("@Nome do seu bot")

def recebendoMsg(msg):
   frase = bot.escuta(frase=msg['text'])
   resp = bot.pensa(frase)
   bot.fala(resp)
   #chatID = msg['chat']['id']
   tipoMsg, tipoChat, chatID = telepot.glance(msg)
   telegram.sendMessage(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
    pass
