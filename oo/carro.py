
GIROS = ['Norte', 'Leste', 'Sul', 'Oeste']

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:
    def __init__(self):
        self.__direcao = 0 # Inicia no Norte
        self.valor = GIROS[self.__direcao]

    def girar_a_direita(self):
        self.__direcao += 1
        if self.__direcao > 3:
            self.__direcao = 0 # Norte
        self.valor = GIROS[self.__direcao]

    def girar_a_esquerda(self):
        self.__direcao -= 1
        if self.__direcao < 0:
            self.__direcao = 3
        self.valor = GIROS[self.__direcao]

