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

class Direção(self):
    valor = 0
    giro = ['Norte', 'Leste', 'Sul', 'Oeste']

    print(f' giro =  {giro[(valor)]}')


    def girar_a_direita(self):
        Direção.valor += 1
        if Direção.valor > 3:
            Direção.valor = 0
            return Direção.giro[0]
        return Direção.giro[Direção.valor]

    def girar_a_esquerda(self):
        Direção.valor -=1
        if Direção.valor < 0:
            Direção.valor = 3
            return Direção.giro[3]
        return Direção.giro[Direção.valor]

class Mycar:
  def __init__(self, velocidade = 0, valor = 0):
        self.velocidade = Motor.velocidade
        self.valor = Direção.valor

# carro1 = Carro()
# carro1.acelerar_motor()
#  print(Motor.velocidade)

car1 = Mycar()
car1.velocidade
car1.Motor.acelerar()

print(car1.velocidade)

# print(Motor.velocidade)
# print(Direção.valor)
# print()
# Motor.acelerar_motor()
# Motor.acelerar_motor()
#Motor.acelerar_motor()
# Direção.girar_a_direita()

#print(Motor.velocidade)
# print(Direção.valor)
#print()
#Motor.frear_motor()
#print(Motor.velocidade)
#print()
#Motor.frear_motor()
#print(Motor.velocidade)
#print()

# Motor.acelerar_motor()
# print(Motor.velocidade)

