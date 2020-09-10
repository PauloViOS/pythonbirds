class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    paulo = Pessoa(nome='Paulo')
    miguel = Pessoa(paulo, nome='Miguel')
    print(Pessoa.cumprimentar(paulo))
    print(id(paulo))
    print(paulo.cumprimentar())
    print(paulo.nome)
    print(paulo.idade)
    for filho in miguel.filhos:
        print(filho.nome)
    miguel.sobrenome = "Santos"
    del miguel.filhos
    miguel.olhos = 1
    del miguel.olhos
    print(miguel.__dict__)
    print(paulo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(miguel.olhos)
    print(paulo.olhos)
    print(id(Pessoa.olhos), id(miguel.olhos), id(paulo.olhos))
