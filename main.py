import os
import random
import time
from prewier import *
from classes import *
from modulo import *



while True:
    menu()
    op = int(input("Escolhe: "))
    limpar_tela()
    if op == 1:
        criar_cachorro(canil)
    elif op == 2:
        criar_humano(cadeia)
    elif op == 3:
        while True:
            laboratorio_menu()
            lab_escolha = int(input("Escolha: "))
            limpar_tela()
            if lab_escolha == 1:
                visu_humano(cadeia)
            elif lab_escolha == 2:
                visu_cachorro(canil)
            elif lab_escolha == 3:
                mod_human(laboratorio_humano)
            elif lab_escolha == 4:
                mod_cachorro(laboratorio_cachorro)
            elif lab_escolha == 5:
                visu_mod_humano(laboratorio_humano)
            elif lab_escolha == 6:
                visu_mod_cachorro(laboratorio_cachorro)
            elif lab_escolha == 7:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    elif op == 4:
        print("Saindo...")
        break
