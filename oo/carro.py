
GIROS_DIREITA = ['Norte', 'Leste', 'Sul', 'Oeste']
GIROS_ESQUERDA = ['Norte', 'Oeste', 'Sul', 'Leste']

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
        self.valor = GIROS_DIREITA[self.__direcao]

    def girar_a_direita(self):
        self.__direcao += 1
        if self.__direcao > 3:
            self.__direcao = 0 # Norte
        self.valor = GIROS_DIREITA[self.__direcao]

    def girar_a_esquerda(self):
        self.__direcao -= 1

        if self.__direcao < 0:
            self.__direcao = 3
        self.valor = GIROS_ESQUERDA[self.__direcao]

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar() # Observe que o carro delega para o motor acelerar

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def calcular_direcao(self):
        if __name__ == '__main__':
            return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

# direcao = Direcao()
# motor = Motor()

carro = Carro(Direcao(), Motor())
carro.calcular_velocidade()
carro.acelerar()
carro.acelerar()
print(carro.calcular_velocidade())
carro.frear()
print(carro.calcular_velocidade())
carro.calcular_direcao()
carro.girar_a_direita()
carro.girar_a_direita()
print(carro.calcular_direcao())
carro.girar_a_esquerda()
print(carro.calcular_direcao())

