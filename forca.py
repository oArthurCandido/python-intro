""" Forca """


def jogar():
    """ Guess a letter """
    secret_word = ['B', 'I', 'R', 'T', 'H', 'D', 'A', 'Y']

    letters_guessed = []

    for letter in range(0, len(secret_word)):
        print("Letras já chutadas: ", letters_guessed)
        guess = input("Chute uma letra: ")
        guess = guess.strip().upper()
        if len(guess) > 1:
            print("Ahh isso não vale, digite apenas uma letra")

        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Você acertou uma letra!")
            else:
                print("Você errou uma letra!")
                print("Letras já chutadas: ", letters_guessed)
                print("A palavra secreta é: ", secret_word)
            if (secret_word == letters_guessed):
                print("Você acertou a palavra secreta!")
                break
