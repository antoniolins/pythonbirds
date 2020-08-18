class Motor:
    velocidade = 0
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def acelerar_motor():
        Motor.velocidade += 1
        return Motor.velocidade

    def frear_motor():
        Motor.velocidade -= 2
        if Motor.velocidade < 0:
            Motor.velocidade = 0
        return Motor.velocidade

class Direção:
    valor = 0
    giro = ['N', 'L', 'S', 'O']

    def girar_a_direita():
        Direção.valor += 1
        if Direção.valor > 3:
            Direção.valor = 0
            return Direção.giro[0]
        return Direção.giro[Direção.valor]

    def girar_a_esquerda():
        Direção.valor -=1
        if Direção.valor < 0:
            Direção.valor = 3
            return Direção.giro[3]
        return Direção.giro[Direção.valor]

class Carro(Motor, Direção):
    Motor.acelerar_motor()
    print(Motor.velocidade)

# print(Motor.velocidade)
# print(Direção.valor)
# print()
# Motor.acelerar_motor()
# Motor.acelerar_motor()
Motor.acelerar_motor()
# Direção.girar_a_direita()

print(Motor.velocidade)
# print(Direção.valor)
print()
Motor.frear_motor()
print(Motor.velocidade)
print()
Motor.frear_motor()
print(Motor.velocidade)
print()

# Motor.acelerar_motor()
# print(Motor.velocidade)

