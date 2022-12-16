"""laço for"""


def guess_number():
    """Guess the number"""


TENTATIVAS = 3
rodada = 1

for rodada in range(1, TENTATIVAS + 1):
    print("Tentativa {} de {}".format(rodada,  TENTATIVAS))
    NUMERO_SECRETO = 42
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
        break

    elif maior:
        print("Você errou pra mais!", )

    elif menor:
        print("Você errou pra menos!")
    rodada = rodada + 1

print("Fim de jogo!")
guess_number()
