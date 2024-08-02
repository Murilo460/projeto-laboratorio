import time
import os
import random
from classes import *
from modulo import *

separar = "==================================================="

def menu():
    print("""
+================MENU================+
|       1 - Criar um Cachorro        |
|       2 - Criar um Humano          |
|       3 - Ir ao Laboratorio        |
|       4 - Sair                     |
+====================================+          
""")
    

def laboratorio_menu():
    print("""
+=================LABORATORIO=================+
|       1 - Visualizar cela de Humanos        |
|       2 - Visualizar cela de Cachorro       |
|       3 - Criar Humano modificado           |
|       4 - Criar Cachorro modificado         |
|       5 - Visualizar Humanos Modificados    |
|       6 - Visualizar Cachorro Modificados   |
|       7 - Sair                              |
+==============================================+          
""")


def visu_humano(cadeia):#Visualizar humano normal
    print(separar)
    for i in range(len(cadeia)):
        print(f"{i+1} - Nome: {cadeia[i].nome}  |   Peso: {cadeia[i].peso}Kg")
    print(separar)
    hs = int(input("Selecione a especime: ")) #HS = humano selecionado
    humano_selecionado = cadeia[hs - 1]
    print(separar)
    print(f"Nome: {humano_selecionado.nome}\nRaça: {humano_selecionado.raca}\nIdade {humano_selecionado.idade}\nPeso: {humano_selecionado.peso}\nTamanho: {humano_selecionado.tamanho}\nCor: {humano_selecionado.cor}\nSexo: {humano_selecionado.sexo}")
    print(separar)
    press_enter()
    limpar_tela()


def visu_cachorro(canil):#Visualizar cachorro normal
    print(separar)
    for i in range(len(canil)):
        print(f"{i+1} - Nome: {canil[i].nome}  |   Peso: {canil[i].peso}Kg")
    print(separar)
    cs = int(input("Selecione a especime: ")) #CS = cachorro selecionado
    cachorro_selecionado = canil[cs - 1]
    print(separar)
    print(f"Raça: {cachorro_selecionado.raca}\nIdade: {cachorro_selecionado.idade}\nPeso: {cachorro_selecionado.peso}\nTamanho: {cachorro_selecionado.tamanho}\nCor: {cachorro_selecionado.cor}\nSexo: {cachorro_selecionado.sexo}\nVacinado: {cachorro_selecionado.vacinado}")
    print(separar)
    press_enter()
    limpar_tela()


def visu_mod_humano(laboratorio_humano):#Visualizar humano modificado
    print(separar)
    for i in range(len(laboratorio_humano)):
        print(f"{i+1} - Nome: {laboratorio_humano[i].nome}  |   Peso: {laboratorio_humano[i].peso}Kg")
    print(separar)
    hs = int(input("Selecione a especime: ")) #HS = humano selecionado
    humano_selecionado = laboratorio_humano[hs - 1]
    print(separar)
    print(f"Nome: {humano_selecionado.nome}\nIdade {humano_selecionado.idade}\nPeso: {humano_selecionado.peso}\nTamanho: {humano_selecionado.tamanho}\nCor: {humano_selecionado.cor}\nSexo: {humano_selecionado.sexo}")
    print(separar)
    press_enter()
    limpar_tela()


def visu_mod_cachorro(laboratorio_cachorro):#Visualizar cachorro modificado
    print(separar)
    for i in range(len(laboratorio_cachorro)):
        print(f"{i+1} - Nome: {laboratorio_cachorro[i].nome}  |   Peso: {laboratorio_cachorro[i].peso}Kg")
    print(separar)
    cs = int(input("Selecione a especime: ")) #CS = cachorro selecionado
    cachorro_selecionado = laboratorio_cachorro[cs - 1]
    print(separar)
    print(f"Raça: {cachorro_selecionado.raca}\nIdade: {cachorro_selecionado.idade}\nPeso: {cachorro_selecionado.peso}\nTamanho: {cachorro_selecionado.tamanho}\nCor: {cachorro_selecionado.cor}\nSexo: {cachorro_selecionado.sexo}\nVacinado: {cachorro_selecionado.vacinado}")
    print(separar)
    press_enter()
    limpar_tela()
    
    




