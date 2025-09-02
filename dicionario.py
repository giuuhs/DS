import os
os.system('cls')

def menu():
    while True:
        print("MENU PRINCIPAL")
        print("----------------")
        print("1 - Criar estrutura do dicionário")
        print("2 - Listar estrutura do dicionário")
        print("3 - Cadastrar registros")
        print("4 - Exibir registros")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            estrutura = criar_estrutura()
        elif opcao == "2":
            listar_estrutura(estrutura)
        elif opcao == "3":
            if estrutura:
                registros.append(cadastrar_registro(estrutura))
            else:
                print("\nCrie a estrutura primeiro (opção 1).\n")
        elif opcao == "4":
            exibir_tabela(estrutura, registros)
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida!\n")

def criar_estrutura():
    estrutura = []
    while True:
        print("\nCRIANDO O DICIONARIO")
        print("--------------------")
        campo = input("\nPonto (.) para finalizar...\nCampo: ")
        if campo == ".":
            break

        print("Tipo:")
        print("1 -> str")
        print("2 -> int()")
        print("3 -> float()")
        escolha = input("Escolha: ")

        if escolha == "1":
            estrutura.append((campo, "str"))
        elif escolha == "2":
            estrutura.append((campo, "int"))
        elif escolha == "3":
            estrutura.append((campo, "float"))
        else:
            print("\nTipo inexistente!")
            continue

        listar_estrutura(estrutura)
    return estrutura

def listar_estrutura(estrutura):
    print("\nESTRUTURA:")
    print("---------")
    for campo, tipo in estrutura:
        print(f"Campo -> {campo:<10} : Tipo -> {tipo}")
    print()

def cadastrar_registro(estrutura):
    registro = {}
    print("\nPREENCHENDO OS REGISTROS:")
    print("-------------------------")
    for campo, tipo in estrutura:
        while True:
            valor = input(f"{tipo:<3} | {campo:<8} -> ")
            try:
                if tipo == "int":
                    registro[campo] = int(valor)
                elif tipo == "float":
                    registro[campo] = float(valor)
                else:
                    registro[campo] = valor
                break
            except:
                print("Valor inválido, tente de novo.")
    print("\nRegistro inserido com sucesso!\n")
    return registro

def exibir_tabela(estrutura, registros):
    print("\nEXIBINDO A TABELA:")
    print("------------------")
    for i, reg in enumerate(registros, start=1):
        print(f"Registro {i}")
        for campo, _ in estrutura:
            pontos = "." * (15 - len(campo))
            print(f"{campo}{pontos}: {reg[campo]}")
        print()

estrutura = []
registros = []

comecar = True
if comecar == True:
    menu()