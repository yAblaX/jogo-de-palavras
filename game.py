# Python - Código

# Imports
from modulo import tamanho, titulo
from time import sleep
from os import system
from random import choice
from keyboard import block_key, unblock_key

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

lista_palavras_facil = ["banana","laranja","uva","morango"]
lista_palavras_medio = ["pera", "manga", "abacaxi", "limao", "kiwi"]
lista_palavras_dificil = ["rambutao", "pitaya", "cherimoya", "physalis", "jabuticaba"]
lista_palavras_impossivel = ["salak", "kiwano", "durian"]

vidas_facil = 20
vidas_medio = 16
vidas_dificil = 12
vidas_impossivel = 6

dificuldade = "M"
# Loop do Jogo
while True:

    # Menu Principal do Jogo
    system("cls")
    print(titulo("Jogo de Advinhação"))
    print("Escolha uma das opções abaixo:")
    print("[1] Jogar")
    print("[2] Regras")

    if dificuldade == "F":
        print("[3] Dificuldade (Atual: Fácil)")
    elif dificuldade == "M":
        print("[3] Dificuldade (Atual: Média)")
    elif dificuldade == "D":
        print("[3] Dificuldade (Atual: Difícil)")
    elif dificuldade == "I":
        print("[3] Dificuldade (Atual: Impossível)")

    print("[4] Sair")
    print("-" * len(titulo("Jogo de Advinhação")))

    # Recebe a resposta e trata possiveis erros
    resposta = input("Digite: ")
    if resposta == "":
        system("cls")
        block_key("enter")
        print("Digite algum número!")
        sleep(3)
        unblock_key("enter")
        continue

    try:
        resposta = int(resposta)
    except ValueError:
        block_key("enter")
        system("cls")
        print("Digite apenas números!")
        sleep(3)
        unblock_key("enter")
        continue

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Inicia uma Partida
    if resposta == 1:
            
        # Muda a lista de palavras baseado na dificuldade
        if dificuldade == "F":
            lista_palavras = list(lista_palavras_facil)
        elif dificuldade == "M":
            lista_palavras = list(lista_palavras_medio)
        elif dificuldade == "D":
            lista_palavras = list(lista_palavras_dificil)
        elif dificuldade == "I":
            lista_palavras = list(lista_palavras_impossivel)

        # Variaveis Base do Jogo
        palavra_secreta = choice(lista_palavras).upper()
        letras_acertadas = ""
        palavra_formada = ""

        # Loop da Partida
        while True:

            # Reset a "palavra_formada" para não acumular caracteres
            palavra_formada = ""
            
            # Cria a "palavra_formada" verificando a "palavra_secreta" e as "letras_acertadas"
            for letra_secreta in palavra_secreta:
                if letra_secreta in letras_acertadas:
                    palavra_formada += letra_secreta
                else:
                    palavra_formada += "*"

            # Verifica se a "palavra_formada" é igual a "palavra_secreta", se for finaliza o jogo com uma vitória
            if palavra_formada == palavra_secreta:
                system("cls")
                print(f"{"=" * 10} VOCÊ GANHOU!!! {"=" * 10}")
                print(f"A palavra era: \"{palavra_secreta}\"\n")
                sleep(5)
                break

            # Limpa o console
            system("cls")

            # Menu da Partida
            print(titulo("Jogo de Advinhação"))
            print(f"Palavra: {palavra_formada}")
            letra_digitada = input("Digite uma letra: ").upper()

            if tamanho(letra_digitada) > 1: 
                # Corrige erro de excesso de caracteres
                block_key("enter")
                system("cls")
                print("Digite apenas uma letra!")
                sleep(3)
                unblock_key("enter")
                pass
            elif tamanho(letra_digitada) == 0: 
                # Corrige erro de falta de caracteres
                block_key("enter")
                system("cls")
                print("Digite pelo menos uma letra!")
                sleep(3)
                unblock_key("enter")
                pass

            if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    elif resposta == 2:
        system("cls")
        print(titulo("regras"))
        print("1°| Não use acentos")
        print("2°| Escreva apenas uma letra por vez")
        print("3°| Use apenas letras")
        print("-" * len(titulo("regras")))
        input("\"ENTER\" para voltar ao menu.\n")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    elif resposta == 3:
        system("cls")
        print(titulo("dificuldade"))
        print("[F] Fácil")
        print("[M] Médio")
        print("[D] Difícil")
        print("[I] Impossível")
        print("-" * len(titulo("dificuldade")))
        dificuldade = input("Digite: ").upper()

        if not dificuldade.isalpha():
            dificuldade = "M"
            system("cls")
            print("Digite uma opção valida!")
            sleep(3)
        
        if dificuldade == "F":
            system("cls")
            print("Dificuldade alterada para \"FÁCIL\"!")
            sleep(3)
        elif dificuldade == "M":
            system("cls")
            print("Dificuldade alterada para \"MÉDIA\"!")
            sleep(3)
        elif dificuldade == "D":
            system("cls")
            print("Dificuldade alterada para \"DIFÍCIL\"!")
            sleep(3)
        elif dificuldade == "I":
            system("cls")
            print("Dificuldade alterada para \"IMPOSSÍVEL\"!")
            sleep(3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    elif resposta == 4:
        system("cls")
        print("Obrigado por jogar!")
        sleep(3)
        system("cls")
        break

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    elif resposta <= 0 and resposta >= 5:
        unblock_key("enter")
        system("cls")
        print("Digite uma opção válida!")
        sleep(3)
        block_key("enter")
        pass
