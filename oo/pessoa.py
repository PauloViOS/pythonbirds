class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3



if __name__ == '__main__':
    paulo = Mutante(nome='Paulo')
    miguel = Homem(paulo, nome='Miguel')
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
    print(Pessoa.olhos)
    print(miguel.olhos)
    print(paulo.olhos)
    print(id(Pessoa.olhos), id(miguel.olhos), id(paulo.olhos))
    print(Pessoa.metodo_estatico(), miguel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), miguel.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(paulo,Pessoa))
    print(isinstance(paulo,Homem))
    print(paulo.olhos)
    print(miguel.cumprimentar())
    print(paulo.cumprimentar())
