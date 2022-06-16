#Trabalho Jogo Jokenpô
#Grupo: Arthur Neumann Salerno - João Gabriel Pitol

import random

#Variável que dita qual o modo escolhido pelo usuário.
#JxJ = Jogador x Jogador
#JxC = Jogador x Computador

JxJ = False
JxC = False

#Pontuação dos Jogadores (pontuação 2 se torna do computador caso seja contra computador).
pontuacao_p1 = 0
pontuacao_p2 = 0

#Variável que guarda a escolha entre 1, 2 e 3.
jogada_1 = -1
jogada_2 = -1

#Variável que dita se o usuário está ou não no menu.
menu = True

#Variavel para pegar o input do usuário.
opcao_menu = -1

while menu == True:
    print("JOKENPÔ")
    print("-------------------------")
    print("Selecione o modo de jogo:")
    print(" ")
    print("1. Jogador x Jogador")
    print("2. Jogador x Computador")
    print("0. Sair")
    print(" ")
    opcao_menu = int(input())

    if opcao_menu == 0:
        menu = False

    if opcao_menu == 1:
        menu = False
        JxJ = True

    if opcao_menu == 2:
        menu = False
        JxC = True

while JxJ == True:
    print("------PLACAR------")
    print("Jogador 1: ", pontuacao_p1)
    print("Jogador 2: ", pontuacao_p2)
    print("------------------")
    print("1. Pedra / 2. Papel / 3. Tesoura / 0. Sair")
    print(" ")
    print("Escolha sua jogada (Jogador 1): ")
    jogada_1 = int(input())
    print("Escolha sua jogada (Jogador 2): ")
    jogada_2 = int(input())

    #Se um dos jogadores digitar 0, acaba o jogo.
    if jogada_1 == 0:
        JxJ = False
    elif jogada_2 == 0:
        JxJ = False

    #Checa se foram digitado números válidos para as seleções.
    #Caso o contrário os números são solicitados novamente.
    if jogada_1 > 0 and jogada_1 < 4:
        if jogada_2 > 0 and jogada_2 < 4:


            #Empate
            if jogada_1 == jogada_2:
                print("Empate")
                print("")

            #Pedra
            if jogada_1 == 1:
                if jogada_2 == 2:
                    pontuacao_p2 += 1
                    print("")
                    print("(Jogador 2 Venceu)")
                    print("")
                if jogada_2 == 3:
                    pontuacao_p1 += 1
                    print("")
                    print("(Jogador 1 Venceu)")
                    print("")

            #Papel
            if jogada_1 == 2:
                if jogada_2 == 1:
                    pontuacao_p1 += 1
                    print("")
                    print("(Jogador 1 Venceu)")
                    print("")
                if jogada_2 == 3:
                    pontuacao_p2 += 1
                    print("")
                    print("(Jogador 2 Venceu)")
                    print("")

            #Tesoura
            if jogada_1 == 3:
                if jogada_2 == 1:
                    pontuacao_p2 += 1
                    print("")
                    print("(Jogador 2 Venceu)")
                    print("")
                if jogada_2 == 2:
                    pontuacao_p1 += 1
                    print("")
                    print("(Jogador 1 Venceu)")
                    print("")



#Contra o Computador
while JxC == True:

    jogada_c = random.randint(1,3)

    print("------PLACAR------")
    print("Jogador: ", pontuacao_p1)
    print("Computador: ", pontuacao_p2)
    print("------------------")
    print("")
    print("1. Pedra / 2. Papel / 3. Tesoura / 0. Sair")
    print("Escolha sua jogada: ")
    jogada_1 = int(input())

    #Se o jogador digitar 0, acaba o jogo.
    if jogada_1 == 0:
        JxC = False

    if jogada_1 > 0 and jogada_1 < 4:
        #Empate
        if jogada_1 == jogada_c:
            print("")
            print("(Empate)")
            print("")

        #Pedra
        if jogada_1 == 1:
            if jogada_c == 2:
                pontuacao_p2 += 1
                print("")
                print("(Computador Venceu)")
                print("")
            if jogada_c == 3:
                pontuacao_p1 += 1
                print("")
                print("(Jogador Venceu)")
                print("")

        #Papel
        if jogada_1 == 2:
            if jogada_c == 1:
                pontuacao_p1 += 1
                print("")
                print("(Jogador Venceu)")
                print("")
            if jogada_c == 3:
                pontuacao_p2 += 1
                print("")
                print("(Computador Venceu)")
                print("")

        #Tesoura
        if jogada_1 == 3:
            if jogada_c == 1:
                pontuacao_p2 += 1
                print("")
                print("(Computador Venceu)")
                print("")
            if jogada_c == 2:
                pontuacao_p1 += 1
                print("")
                print("(Jogador Venceu)")
                print("")

