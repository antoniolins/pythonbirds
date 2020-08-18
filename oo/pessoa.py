class Pessoa:
    olhos = 2  # atributo da class
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod   # Decorator método de classe - Estático
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls): # acessando dados da classe
        return f'{cls} - olhos {cls.olhos}'



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

    luciano.sobrenome = 'Ramalho' '''atributo dinâmico criado exclusivamente para a instância luciano
                                     nenhum outro objeto da classe será afetado. '''
    print(luciano.__dict__) # __dict__ informa todos os atributos do objeto
  #  del luciano.filhos   # o contrário da criação do atributo dinâmico
    luciano.olhos = 1 #
    # del luciano.olhos # Nesse caso estamos apagando um atributo do objeto e não da classe
    print(luciano.__dict__) # checando os atributos de instância
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(f'Pessoa tem olhos = {str(Pessoa.olhos)}')
    print(f'Luciano tem olhos = {str(luciano.olhos)}')
    print(f'Renzo tem olhos = {str(renzo.olhos)}')

    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())

