import os 
os.system("cls")

# 1 -----------------------
def dimensao_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
   
    return linhas, colunas

# 2 -----------------------

def preencher_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = input(f"Digite o dado de posição [{i}] [{j}]: ")
            linha.append(valor)
        matriz.append(linha)
    return matriz

# 3 -----------------------

def exibir_matriz(matriz):
     # Exibindo a matriz
    print("Matriz: ")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()

# 4 -----------------------

def isint(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] in "+-" or s[0] in digito: 
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False
    
    return valido

def lista_numerica(matriz):
    lista = []
    for linha in matriz:
        for item in linha:
            if isint(item):
                lista.append(item)
    return lista

# 5 ----------------------

def lista_naonumerico(matriz):
    lista2 = []
    for linha in matriz:
        for item in linha:
            if not isint(item):
                lista2.append(item)
    return lista2


# MENU
def menu():
    linhas = 0
    colunas = 0
    matriz = [] 
    
    while True:
        print("\n--------------MENU-----------------")
        print("1- Digite as dimensões da sua matriz")
        print("2- Preencha com dados diversos")
        print("3- Exibir sua matriz")
        print("4- Copiar em uma lista os que forem numéricos")
        print("5- Criar outra lista com os dados que não forem numericos")
        print("-----------------------------------")
        escolha = input("\nDigite sua escolha: ")

        if escolha == '1': 
            linhas, colunas = dimensao_matriz()
        elif escolha == '2': 
            matriz = preencher_matriz(linhas, colunas)
        elif escolha == '3': 
            exibir_matriz(matriz)
        elif escolha == '4': 
            lista = lista_numerica(matriz)
            print("Dados numéricos: ", lista)
        elif escolha == '5': 
            lista2 = lista_naonumerico(matriz)
            print("Dados não numéricos: ", lista2)


menu()