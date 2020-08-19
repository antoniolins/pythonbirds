

class Motor:

    velocidade = None

    def __init__(self, velocidade):
        self.velocidade = 0

    def acelerar(self):
        Motor.velocidade += 1
        return Motor.velocidade

    def frear(self):
        Motor.velocidade -= 2
        if Motor.velocidade < 0:
            Motor.velocidade = 0
        return Motor.velocidade

class Direcao:
    giros_a_direita_dct = {'Norte':  'Leste', 'Leste':  'Sul',
                           'Sul': 'Oeste', 'Oeste': 'Norte'}
    giros_a_esquerda_dct = {'Norte': 'Oeste', 'Oeste': 'Sul',
                           'Sul': 'Leste', 'Leste': 'Norte'}

    def __init__(self):
        self.__direcao = 0
        self.valor = giros[self.__direcao]

    # print(f' giro = {giros[self.__direcao]}')

    def girar_a_direita(self):
        self.__direcao += 1
        if self.__direcao > 3:
            self.__direcao = 0
            return giros[0]
        return giros[self.__direcao]

    def girar_a_esquerda(self):
        self.__direcao -= 1
        if self.__direcao < 0:
            self.__direcao = 3
            return giro[3]
        return giros[(self.__direcao)]

