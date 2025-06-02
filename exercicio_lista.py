# Bianca Pereira Cunha e Giulia de Souza Resende

import os
os.system("cls")

def menu():
    print ("----------MENU---------- \n0 - Sair\n\n---LISTAS \n\n1 - Digitar o conteúdo da lista\n2 - Somar os elementos numéricos da lista(int e float)\n3 - Contar quantos elementos str tem na lista")
    print("\n---STRING\n4 - Digitar a frase\n5 - Inverter a frase\n6 - Contar as vogais da frase\n7 - Exibir juntp\n8 - Placa de carro\n9 - CPF válido")
    n = (input("\nEscolha: "))

# 1__________________________

def preenche_lista(lista: list) -> None:
    print("Digite . para terminar sua lista")
    while True:
        lista = list()
        lista = []
        lista = (input("Digite sua lista:"))
        if lista == 0:
            break
        
