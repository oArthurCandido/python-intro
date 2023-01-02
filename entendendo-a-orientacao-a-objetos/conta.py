""" class exemplo"""


class Conta:
    """Define account"""

    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_limite(self):
        return self.__limite

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        limite_antigo = self.__limite
        self.__limite = limite
        print('Limite alterado com sucesso de: {} para: {}'.format(
            limite_antigo, limite))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome_e_sobrenome(self):
        print("{0} {1}".format(self.nome, self.sobrenome))


class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area
