# -*- coding: utf-8 -*-

import json
import sys
import os
import subprocess as s

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            memoria = open(nome+'.json','w')
            memoria.write('[["Neville", "neville"],{"oi": "Olá, qual o seu nome?", "tchau": "Até mais :]"}]')
            memoria.close()
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None]

    def escuta(self,frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        if 'abrindo ' in frase:
            return frase
        frase = frase.lower()
        frase = frase.replace('eh', 'é')
        return frase

    def pensa(self,frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprender':
            return 'Diga o que quer que eu aprenda :] '

        # responde frases que dependem do historico
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Diga o que quer que eu aprenda :] ':
            self.chave = frase
            return 'Diga o que quer que eu responda :] '
        if ultimaFrase == 'Diga o que quer que eu responda :] ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Pronto... Aprendi ;]'

        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
        return 'Não entendi!'


    def pegaNome(self,nome):
        if 'o meu nome é ' in nome:
          nome = nome[13:]

        nome = nome.title()
        return nome

    def respondeNome(self,nome):

        if nome in self.conhecidos:
            frase = 'Bem-Vindo de volta Sr.(a) '
        else:
            frase = 'Prazer em ti conhecer '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase + nome
    
    def gravaMemoria(self):
        memoria = open(self.nome+'.json','w')
        json.dump([self.conhecidos,self.frases],memoria)
        memoria.close()

    def fala(self,frase):
        if 'abrindo ' in frase:
            plataforma = sys.platform
            comando = frase.replace('abrindo ','')
            if 'win' in plataforma:
                os.startfile(comando.lower())
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open',comando])
        else:
            print(frase)
        self.historico.append(frase)
