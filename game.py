# Jogo de advinhação de palavras em Python

# Imports
from modulo import tamanho, titulo
from time import sleep
from os import system
from random import choice
from keyboard import block_key, unblock_key

# Variáveis e listas base
lista_palavras_facil = ["banana","laranja","uva","morango"]
lista_palavras_medio = ["pera", "manga", "abacaxi", "limao", "kiwi"]
lista_palavras_dificil = ["rambutao", "pitaya", "cherimoya", "physalis", "jabuticaba"]
lista_palavras_impossivel = ["salak", "kiwano", "durian"]
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

    # Inicia uma Partida
    if resposta == 1:
            
        # Muda a lista de palavras baseado na dificuldade
        if dificuldade == "F":
            lista_palavras = list(lista_palavras_facil)
            chances = 12
        elif dificuldade == "M":
            lista_palavras = list(lista_palavras_medio)
            chances = 10
        elif dificuldade == "D":
            lista_palavras = list(lista_palavras_dificil)
            chances = 8
        elif dificuldade == "I":
            lista_palavras = list(lista_palavras_impossivel)
            chances = 6

        # Variaveis Base do Jogo
        palavra_secreta = choice(lista_palavras).upper()
        letras_acertadas = ""
        letras_tentadas = ""
        palavra_formada = ""
        tentativas = 0

        # Loop da Partida
        while True:

            # Reset a "palavra_formada" para não acumular caracteres
            palavra_formada = ""
            alfabeto_formado = ""
            
            # Cria a "palavra_formada" verificando a "palavra_secreta" e as "letras_acertadas"
            for letra_secreta in palavra_secreta:
                if letra_secreta in letras_acertadas:
                    palavra_formada += letra_secreta
                else:
                    palavra_formada += "*"
            
            # Cria o "alfabeto_formado" verificando as "letras_tentadas" e o "alfabeto"
            for letra in alfabeto:
                if letra in letras_tentadas:
                    alfabeto_formado += letra
                else:
                    alfabeto_formado += "_"
            
            # Cria uma tela de derrota e trata possíveis erros povenientes do usuário
            if chances == 0:
                while True:
                    system("cls")
                    titulo("derrota")
                    print("Escolha uma opção:")
                    print("[1] Ver palavra secreta")
                    print("[2] Voltar para o menu")
                    print("-" * len(titulo("derrota")))

                    try:
                        resposta_derrota = int(input("Digite: "))
                    except:
                        block_key("ENTER")
                        system("cls")
                        print("Digite uma opção válida!1")
                        sleep(3)
                        unblock_key("ENTER")
                        continue

                    if resposta_derrota < 1 or resposta_derrota > 2:
                        block_key("ENTER")
                        system("cls")
                        print("Digite uma opção válida!2")
                        sleep(3)
                        unblock_key("ENTER")
                        continue

                    if resposta_derrota == 1:
                        system("cls")
                        print(titulo("derrota"))
                        print(f"A palavra secreta era: \"{palavra_secreta}\"")
                        print("-" * len(titulo("derrota")))
                        input("Pressione ENTER para voltar para o menu: ")
                        break
                    elif resposta_derrota == 2:
                        break
                break

            # Verifica se a "palavra_formada" é igual a "palavra_secreta", se for, finaliza o jogo com uma vitória
            if palavra_formada == palavra_secreta:
                system("cls")
                print(titulo("vitória!"))
                print(f"A palavra era: \"{palavra_secreta}\"")
                print(f"Você acertou com {tentativas} tentativas!")
                print("-" * len(titulo("vitoria!")))
                input("\"ENTER\" para voltar ao menu.\n")
                break

            # Menu da Partida
            system("cls")
            print(titulo("Jogo de Advinhação"))
            print(f"Palavra: {palavra_formada}{" " * 26}Chances: {chances}") # espaçar pelo tamanho, usando aquelas merdas lá de (*><^:..)

            print(f"Letras tentadas: {alfabeto_formado}")

            print("-" * len(titulo("Jogo de Advinhação")))
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

            if letra_digitada in alfabeto_formado:
                pass
            elif letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada
                alfabeto_formado += letra_digitada
                letras_tentadas += letra_digitada
                tentativas += 1
            else:
                letras_tentadas += letra_digitada
                tentativas += 1
                chances -= 1

    elif resposta == 2:
        # Mostra as regras do jogo
        system("cls")
        print(titulo("regras"))
        print("1°| Não use acentos")
        print("2°| Escreva apenas uma letra por vez")
        print("3°| Use apenas letras")
        print("-" * len(titulo("regras")))
        input("\"ENTER\" para voltar ao menu.\n")

    elif resposta == 3:
        # Altera a dificuldade do jogo
        system("cls")
        print(titulo("dificuldade"))
        print("[F] Fácil")
        print("[M] Médio")
        print("[D] Difícil")
        print("[I] Impossível")
        print("-" * len(titulo("dificuldade")))
        dificuldade = input("Digite: ").upper()

        if not dificuldade.isalpha():
            block_key("enter")
            dificuldade = "M"
            system("cls")
            print("Digite uma opção valida!")
            sleep(2)
            unblock_key("enter")

        if dificuldade == "F":
            block_key("enter")
            system("cls")
            print("Dificuldade alterada para \"FÁCIL\"!")
            sleep(3)
            unblock_key("enter")
        elif dificuldade == "M":
            block_key("enter")
            system("cls")
            print("Dificuldade alterada para \"MÉDIA\"!")
            sleep(3)
            unblock_key("enter")
        elif dificuldade == "D":
            block_key("enter")
            system("cls")
            print("Dificuldade alterada para \"DIFÍCIL\"!")
            sleep(3)
            unblock_key("enter")
        elif dificuldade == "I":
            block_key("enter")
            system("cls")
            print("Dificuldade alterada para \"IMPOSSÍVEL\"!")
            sleep(3)
            unblock_key("enter")
        else:
            block_key("enter")
            system("cls")
            print("Digite uma opção valida!")
            sleep(3)
            unblock_key("enter")

    elif resposta == 4:
        # Sai do programa
        system("cls")
        print("Obrigado por jogar!")
        sleep(3)
        system("cls")
        break

    else:
        # Caso outro número além de [1,2,3,4] tenha sido digitado, ele gera um aviso
        block_key("enter")
        system("cls")
        print("Digite uma opção válida!")
        sleep(3)
        unblock_key("enter")
        pass
