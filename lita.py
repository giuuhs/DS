import os
os.system

lista = list()
lista = []
lista = ["giu_bibia", 1, True]

lista [3] = 4
print(lista)
lista.append("Novo") # append () insere um elemento no final da lista
print(lista)

print(lista)
lista.insert(2, 99.9) # append (posição, elemento) insere um elemento em alguma posição
print(lista)

#pop(posição) - remove um elemento pela posição 
"""
os system ("cls")
print(lista)
lista.pop()
print(lista)
lista.pop(2)
print(lista)
""" 

#remove - remove pelo elemento
lista = ["giu_bibia", 1, True, 1]
os.system ("cls")
print("Antes: ", lista)
lista.remove(3)
print ("Depois: ", lista)

#index(elemento) - retorna o indice do elemento passado pelo parametro
lista = ["giu_bibia", 1, True]
os.system ("cls")
ind = lista.index(1)
print ("Indice: ", ind)

#count(elemento) - conta a incidência de elemento na lista
lista = ["giu_bibia", 1, True, 1]
os.system
qtd = lista.count(5)
print ("quantidade: ", qtd)

#FUNÇÃO len(lista) - conta a quantidade de elemento na lista
lista = ["giu_bibia", 1, True, 1]
os.system
qtd = lista.count(5)
print ("quantidade: ", qtd)

#concatenação
lista1 = [12,22,65,88]
lista2 = [33,23]
lista3 = lista1 = lista2
print(lista1)
print(lista2)
print(lista3)

# extended() - adiciona uma lista no final da outra
lista1 = [12,22,65,88]
lista2 = [33,23]
print(lista1)
print(lista2)
lista1.extend(lista2)
print(lista1)
print(lista2)

# copy() - efetua a copia de uma lista
