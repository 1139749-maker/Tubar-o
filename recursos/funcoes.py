import os, time 
import json


def escreverDados(nome, pontos, data):
    
    try:
        banco = open("base.atitus", "r")
        dados = banco.read()
        banco.close()
    except FileNotFoundError:
        dados = ""
        
    if dados != "":
        try:
            dadosDict = json.loads(dados)
        except json.JSONDecodeError:
            dadosDict = {} 
    else:
        dadosDict = {}
        
    if nome not in dadosDict or pontos > dadosDict[nome][0]:
        dadosDict[nome] = [pontos, data]
    
    banco = open("base.atitus", "w")
    banco.write(json.dumps(dadosDict))
    banco.close()
    
def maior_pontuador():
    try:
        banco = open("base.atitus", "r")
        dados = banco.read()
        banco.close()
    except FileNotFoundError:
        dados = ""
        
    if dados != "":
        try:
            dadosDict = json.loads(dados)
        except json.JSONDecodeError:
            dadosDict = {} 
    else:
        dadosDict = {}

    nome_maior = None
    dataJogada = None
    maior_pontos = -1

    for nome, info in dadosDict.items():
        pontos = info[0]
        if pontos > maior_pontos:
            maior_pontos = pontos
            nome_maior = nome
            dataJogada = info[1]            

    if nome_maior is None:
        return None, 0, None

    return nome_maior, maior_pontos, dataJogada