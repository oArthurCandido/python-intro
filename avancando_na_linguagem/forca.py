def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ['_' for _ in range(len(palavra_secreta))]

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)


if __name__ == "__main__":
    jogar()
