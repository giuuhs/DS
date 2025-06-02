import os
os.system ("cls")
"""lista1 = [1, 2, 3]
lista2 = lista1
print(lista1)
print (lista2)
lista1[0] = 99
print(lista1)
print (lista2) """

# copy() - cria copia independente de uma lista 
lista1 = [1, 2, 3, 4]
lista2 = lista1.copy ()
print (lista1)
print (lista2)
lista1 [0] = 99
print(lista1)
print (lista2)

# método sort()
lista = [7, 3, 9, 8, 1, 2]
print (lista)
#reverse = True - é para inverter a ordem para decrescente
lista.sort(reverse = True)
print (lista)

#método reverse()
lista = [7, 3, 9, 8, 1, 2]
print (lista)
lista.reverse()
print (lista)

# método clear()
os.system("cls")
lista = [7, 3, 9, 8, 1, 2]
print (lista)
#del lista - ele deleta o atributo lista, ele continua ali mas não é mais utilizável
lista.clear()
print (lista)
