# Giulia de Souza e Bianca Pereira

import os
os.system("cls")
lista = []

def isfloat(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-','',1)
    elif v[0] == '+':
        v = v.replace('+','',1)
        v = v.replace('.','',1)
    return v.isdigit()
def isint(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] in "+-" or s[0] in digito:
        for i in range (1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False
    return valido

def preencher_lista(lista: list) -> None:
    while True:
        elem = input("Elemento: ")
        if elem == ".":
            break
        else:
            lista.append(elem)
    print(lista)

def somar_elementos(lista: list) -> float:
    soma = 0
    for elem in lista:
        if isfloat(elem) or isint(elem):
            num = float (elem)
            soma += num
    return soma

def contar_str(lista: list) -> int:
    qtd = 0
    for elem in lista:
        a = isfloat(elem)
        b = isint(elem)
        if  a == False and b == False:
            qtd = qtd +  1
    return qtd

def inverter_frase(frase: str) -> str:
    return frase[::-1]

def contar_vogal(frase: str) -> int:
    vogal = "AEIOU"
    qtd = 0
    for letra in frase:
        if letra.upper() in vogal:
            qtd = qtd + 1
    return qtd

def exibir_junto(frase: str) -> None:
    return frase.replace(" ", "")

def isplaca(placa: str) -> bool:
    if len(placa) <= 7:
        digito = "0123456789"
        valido = True
        for i in range(0,3):
            if placa[i] in digito:
                valido = False
        if placa[3] not in digito:
            valido = False
        if placa[5] not in digito:
            valido = False
        if placa[6] not in digito:
            valido = False
    elif len(placa) > 7:
        valido = False
    return valido

def iscpf(cpf: str)-> bool:
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True


while True:
    print("""
MENU
      
0 - SAIR

SOBRE LISTAS
1 - Digitar o conteúdo da lista
2 - Somar os elementos numéricos da lista (int e float)
3 - Contar quantos elementos str tem na lista


SOBRE STRINGS
4 - Digitar a frase
5 - Inverter a frase
6 - Contar as vogais da frase
7 - Exibir junto
8 - Placa de carro      
9 - CPF Válido

            
    """)

    escolha = int(input("Escolha: "))
    if escolha == 0:
        break
    if escolha == 1:
        preencher_lista(lista)
    if escolha == 2:
        print(f"Soma dos elementos: {somar_elementos(lista)}")
    if escolha == 3:
        print(f"Quantidade de strings: {contar_str(lista)}")
    if escolha == 4:
        frase = str(input("Frase: "))
    if escolha ==5:
        print(f"Frase invertida: {inverter_frase(frase)}")
    if escolha == 6:
        print(f"Quantidade de Vogais: {contar_vogal(frase)}")
    if escolha == 7:
        print(f"Frase sem espaços: {exibir_junto(frase)}")
    if escolha ==8:
        placa = input("Digite a sua placa de carro: ")
        print(f"É uma placa de carro: {isplaca(placa)}")
    if escolha ==9:
        cpf = input("Digite seu cpf: ")
        print(f"É um cpf: {iscpf(cpf)}")
    

