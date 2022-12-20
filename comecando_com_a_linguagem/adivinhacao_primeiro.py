'''
Jogo de adivinhação
'''
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")


def guess_number():
    """Guess the number"""


TENTATIVAS = 3
rodada = 1

while rodada <= TENTATIVAS:
    print("Tentativa {} de {}".format(rodada,  TENTATIVAS))
    NUMERO_SECRETO = 42
    chute = input("Digite o seu numero: ")
    numero = int(chute)
    acertou = NUMERO_SECRETO == numero
    maior = NUMERO_SECRETO < numero
    menor = NUMERO_SECRETO > numero

    if acertou:
        print("Você acertou!")
        print("Fim de jogo!")
        rodada = 4

    elif maior:
        print("Você errou pra mais!", )

    elif menor:
        print("Você errou pra menos!")

    rodada = rodada + 1

    if rodada == 4:
        print("Fim de jogo!")


guess_number()

# minha_idade = 26
# idade_namorado = 26
# if (minha_idade == idade_namorado):
#     print('temos idades iguais')
# else:
#     print('temos idades diferentes')


# numero1 = 10
# numero2 = 10
# if (numero1 == numero2):
#     print("São números iguais")


# nome = "Nico"
# sobrenome = "Steppat"
# print(nome + sobrenome)
