class Animal:
    nome = ""
    idade = 0
    coração = True
    racionalidade = True
    cor = ""
    peso = 0.0
    tamanho = 0.0
    sexo = ""
    raca = ""
    


class Human(Animal):
    nivel_etico = 0
    
    def __init__(self, raca, idade, peso, tamanho, cor, sexo, vacinado, nome):
        self.raca = raca
        self.idade = idade
        self.peso = peso
        self.tamanho = tamanho 
        self.cor = cor
        self.sexo = sexo
        self.vacinado = vacinado
        self.nome = nome
        self.coração = True
        self.racionalidade = True
    

class Cachorro(Animal):
    vacinado = False
    

    def __init__(self, raca, idade, peso, tamanho, cor, sexo, vacinado, nome):
        self.raca = raca
        self.idade = idade
        self.peso = peso
        self.tamanho = tamanho 
        self.cor = cor
        self.sexo = sexo
        self.vacinado = vacinado
        self.nome = nome
        self.coração = True
        self.racionalidade = False
