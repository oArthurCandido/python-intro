""" Random number guessing game """

import random

"""laço for"""


def guess_number():
    """Guess the number"""


TENTATIVAS = 0
rodada = 1
NUMERO_SECRETO = random.randrange(1, 100)
SCORE = 1000
ACERTOU = False

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))
if (nivel == 1):
    TENTATIVAS = 20
elif (nivel == 2):
    TENTATIVAS = 10
else:
    TENTATIVAS = 5


for rodada in range(1, TENTATIVAS + 1):
    print("Tentativa {} de {}".format(rodada,  TENTATIVAS))

    chute = input("Digite o seu numero: ")
    numero = int(chute)
    if (numero < 1 or numero > 100):
        print("Você deve digitar um número entre 1 e 100!")

        continue
    acertou = NUMERO_SECRETO == numero
    maior = NUMERO_SECRETO < numero
    menor = NUMERO_SECRETO > numero

    if acertou:
        print("Você acertou!")
        ACERTOU = True
        break

    elif maior:
        SCORE = SCORE - abs(NUMERO_SECRETO - numero)
        print("Você errou pra mais!", )

    elif menor:
        print("Você errou pra menos!")
        SCORE = SCORE - abs(NUMERO_SECRETO - numero)
    rodada = rodada + 1
if (ACERTOU == False):
    print("Fim de jogo, o palpite correto era {}!".format(NUMERO_SECRETO))
else:
    print("Fim de jogo, o palpite correto era {}!. Sua pountação foi: {}".format(
        NUMERO_SECRETO, SCORE))
guess_number()
