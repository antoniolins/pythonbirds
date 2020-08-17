class Pessoa:
    olhos = 2  # atributo da class
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')

    print(luciano.__dict__)

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome, luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho' # atributo dinâmico
    print(luciano.__dict__)
  #  del luciano.filhos   # o contrário da criação do atributo dinâmico
    luciano.olhos = 1 #
    # del luciano.olhos
    print(luciano.__dict__) # checando os atributos de instância
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(f'Pessoa tem olhos = {str(Pessoa.olhos)}')
    print(f'Luciano tem olhos = {str(luciano.olhos)}')
    print(f'Renzo tem olhos = {str(renzo.olhos)}')

    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
