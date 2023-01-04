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

    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou seu saldo {} somado com seu limite {}, você pode sacar até {}".format(
                valor, self.saldo, self.limite, (self.limite + self.saldo)))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        limite_antigo = self.__limite
        self.__limite = limite
        print('Limite alterado com sucesso de: {} para: {}'.format(
            limite_antigo, limite))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


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
