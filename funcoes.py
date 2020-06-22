# -*- coding: utf-8 -*-

def resposta():
    #capturando a resposta do usuario e processando-a
    resp = input('>: ')
    resp = resp.lower()
    resp = resp.replace('eh', 'é')
    return resp

def pegaNome(nome):
    if 'o meu nome é ' in nome:
        nome = nome[13:]

    nome = nome.title()
    return nome

def respondeNome(nome):
    conhecidos = ['@Coloque nome de conhecidos aqui']

    if nome in conhecidos:
        frase = 'Bem-Vindo de volta Sr(a) '
    else:
        frase = 'Prazer em conhece-lo '

    return frase+nome
