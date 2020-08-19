DIRECOES = ['Norte', 'Leste', 'Sul', 'Oeste']


class Direcao:

    def __init__(self):
        self.__direcao = 0
        self.valor = DIRECOES[self.__direcao]

    def girar_a_direita(self):
        self.__direcao = (self.__direcao + 1) % len(DIRECOES)
        self.valor = DIRECOES[self.__direcao]

    def girar_a_esquerda(self):
        self.__direcao = (self.__direcao - 1) % len(DIRECOES)
        self.valor = DIRECOES[self.__direcao]

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquereda()

