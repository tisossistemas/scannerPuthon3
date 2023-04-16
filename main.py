#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system as os
from sys import exit
from time import sleep
from socket import *


'''
@autor: Prince
@date: 13/02/2017
Scanner de portas criado para rodar em python3
'''


def menu():
    os('cls')
    print('''
    ==== Scanner de portas de sites e IP ====
    @autor  : Prince
    @date   : 13/02/2017
    @version: 1.0.13.2.17
   



    ''')
    try:
        escolha = int(input("Escolha: [1] Escanear  [2] Finalizar script :"))
    except:
        print("\nEscolha invalida")
        sleep(2)
        os('cls')
        menu()
    if escolha == 1:
        escanear()
    elif escolha == 2:
        os("exit")
    else:
        print("\nEscolha invalida")
        sleep(1)
        menu()


def escanear():
    os("cls")
    host = input(" Digite o Nome do site ou host: ")
    executar = 'ping ' + host

    try:
        # realizado um ping no endereco para verificar nossa conectividade, convertemos o endereco para um numero ip
        os(str(executar))
        ip = gethostbyname(host)

        print(f'''
        
Scaner no endereco IP: {ip}
''')
    except:
        # se o endereco for invalido apresentamos um alerta aguardamos alguns segundos limpamos a tela e voltamos para o escaner
        print
        "Host invalido."
        sleep(1)
        os('cls')
        escanear()
    try:
        # pegando a porta inicial
        pi = int(input("Porta inicial (ex: 441): "))
    except:
        # se o numero for invaldio apresentamos um alerta aguardamos alguns segundos e reiniciamos o escaner
        print
        "Porta inicial invalida."
        sleep(1)
        os('cls')
        escanear()
    try:
        # pegando a porta final
        pf = int(input("Porta final (ex: 449): "))
    except:
        # se a porta for invalida apresentamos um alerta aguardamos alguns segundos limpamos a tela e reiniciamos o escaner
        print
        "Porta final invalida."
        sleep(1)
        os('cls')
        escanear()
    # iniciando o escnaeamento no loop entre as portas
    print
    "Iniciando escaneamento ....\n"

    for i in range(pi, pf + 1):
        sckt = socket(AF_INET, SOCK_STREAM)  # criando um socket
        res = sckt.connect_ex((ip, i))  # fazendo a conexao
        if (res == 0):
            print(f"Porta {i} aberta")
        else:
            print(f"Porta {i} fechada ")
        sckt.close()
    print
    "\nEscaneamento finalizado\n"


menu()

