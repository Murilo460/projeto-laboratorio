import os
import time
import random
from classes import *


laboratorio_cachorro = []
laboratorio_humano = []
canil = []
cadeia = []


def press_enter():
    enter = input("Precione Enter: ")
    return enter

def limpar_tela():
    os.system('cls')

def gerar():#Animação de "Gerando..."
    print("Gerando nova especie")
    time.sleep(0.5)
    os.system('cls')
    print("Gerando nova especie.")
    time.sleep(0.5)
    os.system('cls')
    print("Gerando nova especie..")
    time.sleep(0.5)
    os.system('cls')
    print("Gerando nova especie...")
    time.sleep(0.5)
    os.system('cls')
    print("Gerando nova especie")
    time.sleep(0.5)
    os.system('cls')
    print("Gerando nova especie.")
    time.sleep(0.5)
    os.system('cls')
    print("Gerando nova especie..")
    time.sleep(0.5)
    os.system('cls')

separar = "==================================================="

def criar_cachorro(canil):
    print(separar)
    _nome = input("\nNome do cachorro: ")
    _raca = input("Informe a raça do Cachorro: ")
    _idade = int(input("Informe a idade do Cachorro: "))
    _peso = float(input("Informe o peso do Cachorro: "))
    _tamanho = float(input("Informe o tamanho do Cachorro: "))
    _cor = input("Informe a cor do Cachorro: ")
    _sexo = input("Informe o sexo do Cachorro: ")
    _vacinado = input("O Cachorro está vacinado? (S/N)\n")
    if _vacinado == "s" or "S":
        _vacinado = True
    elif _vacinado == "n" or "N":
        _vacinado = False
    else:
        print("Opção inválida. Por favor, digite S ou N.")
    _cachorro = Cachorro(raca = _raca, idade = _idade, sexo = _sexo, cor = _cor, tamanho = _tamanho, peso = _peso, nome = _nome, vacinado = _vacinado)
    canil.append(_cachorro)

def criar_humano(cadeia):
    _vacinado = True
    print(separar)
    _nome_humano = input("\nNome do Humano: ")
    _raca_humano = input("Informe a raça do Humano: ")
    _idade_humano = int(input("Informe a idade do Humano: "))
    _peso_humano = float(input("Informe o peso do Humano: "))
    _tamanho_humano = float(input("Informe o tamanho do Humano: "))
    _cor_humano = input("Informe a cor do Humano: ")
    _sexo_humano = input("Informe o sexo do Humano: ")
    _humano = Human(raca = _raca_humano, idade = _idade_humano, sexo = _sexo_humano, cor = _cor_humano, tamanho = _tamanho_humano, peso = _peso_humano, vacinado = _vacinado, nome = _nome_humano)
    cadeia.append(_humano)


def mod_human(laboratorio_humano):#Criar humano modificado
    print(separar)
    for i in range(len(cadeia)):
        print(f"{i+1} - Nome: {cadeia[i].nome}  |   Peso: {cadeia[i].peso}Kg")
    print(separar)
    cob1 = int(input("Selecione a cobaia N°1: "))
    cobaia_1 = cadeia[cob1 -1]
    print(separar)
    print(f"Nome: {cobaia_1.nome}\nIdade {cobaia_1.idade}\nPeso: {cobaia_1.peso}\nTamanho: {cobaia_1.tamanho}\nCor: {cobaia_1.cor}\nSexo: {cobaia_1.sexo}")
    print(separar)
    press_enter()
    limpar_tela()

    for i in range(len(cadeia)):
        print(f"{i+1} - Nome: {cadeia[i].nome}  |   Peso: {cadeia[i].peso}Kg")
    print(separar)
    cob2 = int(input("Selecione a cobaia N°2: "))
    cobaia_2 = cadeia[cob2 -1]
    print(separar)
    print(f"Nome: {cobaia_2.nome}\nIdade {cobaia_2.idade}\nPeso: {cobaia_2.peso}\nTamanho: {cobaia_2.tamanho}\nCor: {cobaia_2.cor}\nSexo: {cobaia_2.sexo}")
    print(separar)
    press_enter()
    limpar_tela()
    gerar()
    new_raca = input("Nome da nova Raça: ")
    new_nome = input("Nome da Especime: ")
    limpar_tela()
    print(separar)
    print(new_raca)
    new_idade = 1
    time.sleep(1)
    new_peso = cobaia_1.peso + cobaia_2.peso
    print(f"Peso: {new_peso} Kg")
    time.sleep(1)
    new_tamanho = cobaia_1.tamanho + cobaia_2.tamanho
    print(f"Tamanho: {new_tamanho} Cm")
    time.sleep(1)
    new_cor = random.randint(1,3)
    if new_cor < 3:
        new_cor = cobaia_1.cor
    else:
        print("COR RARA!")
        new_cor = "Azul Goiaba"
    new_sexo = random.randint(1,2)
    if new_sexo == 1:
        new_sexo = "Macho"
    else:
        new_sexo = "Fêmea"
    new_vacinado = True
    print(separar)
    press_enter()
    limpar_tela()
    _new_humano = Human(raca = new_raca, idade = new_idade, sexo = new_sexo, cor = new_cor, tamanho = new_tamanho, peso = new_peso, nome = new_nome, vacinado = new_vacinado)
    laboratorio_humano.append(_new_humano)


def mod_cachorro(laboratorio_cachorro):#Criar cachorro modificado
    print(separar)
    for i in range(len(canil)):
        print(f"{i+1} - Nome: {canil[i].nome}  |   Peso: {canil[i].peso}Kg")
    print(separar)
    cob1 = int(input("Selecione a cobaia N°1: "))
    cobaia_1 = canil[cob1 -1]
    print(separar)
    print(f"Raça: {cobaia_1.raca}\nIdade {cobaia_1.idade}\nPeso: {cobaia_1.peso}\nTamanho: {cobaia_1.tamanho}\nCor: {cobaia_1.cor}\nSexo: {cobaia_1.sexo}")
    print(separar)
    press_enter()
    limpar_tela()

    for i in range(len(cadeia)):
        print(f"{i+1} - Nome: {canil[i].nome}  |   Peso: {canil[i].peso}Kg")
    print(separar)
    cob2 = int(input("Selecione a cobaia N°2: "))
    cobaia_2 = canil[cob2 -1]
    print(separar)
    print(f"{i+1} - Raça: {cobaia_2.raca}\nIdade {cobaia_2.idade}\nPeso: {cobaia_2.peso}\nTamanho: {cobaia_2.tamanho}\nCor: {cobaia_2.cor}\nSexo: {cobaia_2.sexo}")
    print(separar)
    press_enter()
    limpar_tela()
    gerar()
    new_raca = input("Nome da nova Raça: ")
    new_nome = input("Nome da Especime: ")
    limpar_tela()
    print(separar)
    print(new_raca)
    new_idade = 1
    time.sleep(1)
    new_peso = cobaia_1.peso + cobaia_2.peso
    print(new_peso)
    time.sleep(1)
    new_tamanho = cobaia_1.tamanho + cobaia_2.tamanho
    print(new_tamanho)
    time.sleep(1)
    new_cor = random.randint(1,3)
    if new_cor < 3:
        new_cor = cobaia_1.cor
    else:
        print("COR RARA!")
        new_cor = "vermelho"
    new_sexo = random.randint(1,2)
    if new_sexo == 1:
        new_sexo = "Macho"
    else:
        new_sexo = "Fêmea"
    new_vacinado = True
    print(separar)
    press_enter()
    limpar_tela()
    _new_cachorro = Cachorro(raca = new_raca, idade = new_idade, sexo = new_sexo, cor = new_cor, tamanho = new_tamanho, peso = new_peso, nome = new_nome, vacinado = new_vacinado)
    laboratorio_cachorro.append(_new_cachorro)