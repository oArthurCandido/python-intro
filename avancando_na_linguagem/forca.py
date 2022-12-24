""" Forca """
import random


def jogar():
    """Jogo da forca"""
    welcome()
    palavra_secreta = set_word()
    letras_acertadas = start_right_words(palavra_secreta)
    letras_chutadas = []

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = set_guess()
        if len(chute) > 1:
            print('Faça o chute com uma letra apenas.')
            continue
        if chute in palavra_secreta:
            set_guess_right(chute, palavra_secreta,
                            letras_chutadas, letras_acertadas)

        else:
            letras_chutadas.append(chute)
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print('Letras chutadas: {}'.format(letras_chutadas))

    if acertou:
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta)


def welcome():
    """ Print welcome message """
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")


def set_word():
    """ Set the secret word to strart the game """
    with open(
            'avancando_na_linguagem\palavras.txt', "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

        numero = random.randrange(0, len(palavras))

        palavra_secreta = palavras[numero].upper()
        return palavra_secreta


def start_right_words(palavra_secreta):
    """ create an array to receive the right letters """
    return ["_" for letra in palavra_secreta]


def set_guess():
    """ input creator"""
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def set_guess_right(chute, palavra_secreta,
                    letras_chutadas, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra

        index += 1
    letras_chutadas.append(chute)


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
