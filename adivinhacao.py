""" Random number guessing game """

import random


def jogar():
    """Guess the number"""
    tentativas = 0
    rodada = 1
    numero_secreto = random.randrange(1, 100)
    score = 1000
    acertou_na_mosca = False

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada,  tentativas))

        chute = input("Digite o seu numero: ")
        numero = int(chute)
        if (numero < 1 or numero > 100):
            print("Você deve digitar um número entre 1 e 100!")

            continue
        acertou = numero_secreto == numero
        maior = numero_secreto < numero
        menor = numero_secreto > numero

        if acertou:
            print("Você acertou!")
            acertou_na_mosca = True
            break

        elif maior:
            score = score - abs(numero_secreto - numero)
            print("Você errou pra mais!", )

        elif menor:
            print("Você errou pra menos!")
        score = score - abs(numero_secreto - numero)
    rodada = rodada + 1
    if acertou_na_mosca is False:
        print("Fim de jogo, o palpite correto era {}!".format(numero_secreto))
    else:
        print("Fim de jogo, o palpite correto era {}!. Sua pountação foi: {}".format(
            numero_secreto, score))


if __name__ == "__main__":
    jogar()
