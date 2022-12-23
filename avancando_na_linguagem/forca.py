""" Forca """
import random


def jogar():
    """Jogo da forca"""
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    with open(
            'avancando_na_linguagem\palavras.txt', "r") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_chutadas = []

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        if len(chute) > 1:
            print('Faça o chute com uma letra apenas.')
            continue
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra

                index += 1
            letras_chutadas.append(chute)

        else:
            letras_chutadas.append(chute)
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print('Letras chutadas: {}'.format(letras_chutadas))

    if acertou:
        print('Parabéns, você acertou com {} erros!'.format(erros))

    else:
        print('Não foi dessa vez =/')


if __name__ == "__main__":
    jogar()
