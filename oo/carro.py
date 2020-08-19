class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
        return self.velocidade

class Direcao:
    valor = 0
    giro = ['Norte', 'Leste', 'Sul', 'Oeste']

    print(f' giro =  {giro[(valor)]}')


    def girar_a_direita(self):
        Direcao.valor += 1
        if Direcao.valor > 3:
            Direcao.valor = 0
            return Direcao.giro[0]
        return Direcao.giro[Direcao.valor]

    def girar_a_esquerda(self):
        Direcao.valor -=1
        if Direcao.valor < 0:
            Direcao.valor = 3
            return Direcao.giro[3]
        return Direcao.giro[Direcao.valor]

class Mycar:
  def __init__(self, velocidade = 0, valor = 0):
        self.velocidade = Motor.velocidade
        self.valor = Direcao.valor

motor = Motor()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)

motor.frear()
print(motor.velocidade)
