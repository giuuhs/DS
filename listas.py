# métodos de listas
import os
os.system("cls")
# copy() - cria a cópia independente de uma lista
lista1 = [1,2,3]
lista2 = lista1.copy()
print(lista1)
print(lista2)
lista1[0] = 99
print(lista1)
print(lista2)

# método sort()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
lista.sort(reverse = True)
print(lista)

# método reverse()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
lista.reverse()
print(lista)

# método clear()
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
lista.clear()
print(lista)

# método del
os.system("cls")
lista = [7,3,9,8,1,2]
print(lista)
del lista

print(lista)

"""
lista1 = [1, 2, 3]
lista2 = lista1
print(lista1)
print(lista2)
lista1[0] = 99
print(lista1)
print(lista2)
"""