

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:
    giros_a_direita_dct = {'Norte':  'Leste', 'Leste':  'Sul',
                           'Sul': 'Oeste', 'Oeste': 'Norte'}
    giros_a_esquerda_dct = {'Norte': 'Oeste', 'Oeste': 'Sul',
                           'Sul': 'Leste', 'Leste': 'Norte'}

    def __init__(self):
        self.__direcao = 0 # Inicia no Norte
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

