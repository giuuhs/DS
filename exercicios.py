# 1. Crie uma função que passe dois valores por parâmetro e exiba o de maior valor 
# 2. Crie uma função que passe tres valores por parâmetro e exiba o de menor valor 
# 3. Crie um procedimento que passe um valor por parâmetro e exiba em ordem decrescente até 0 

import random
import os 
os.system ("cls")

def maior2n(n1: float, n2: float) -> float:
    if n1 > n2:
        return n1
    else:
        return n2

nm1 = random.randint (1, 15)
nm2 = random.randint (1, 15)
#nm3 = random.randint (1, 15)

maior = maior2n(nm1, nm2)
print (f"Foram sorteados os numeros {nm1} e {nm2}.\n")
print (f"O numero maior entre os 2 é: {maior2n}")
'''
def menor3n(n1: float, n2: float, n3:float) -> float:
    if n1 > n2 or n3 > n2:
        return n2
    elif n1 > n3 or n3 < n1:
        return n3
    elif n1 < n3 or n1 < n2:
        return n1
    
menor = menor3n(nm1, nm2, nm3)
print (f"Foram sorteados os numeros {nm1}, {nm2} e {nm3}.\n")
print(f"O menor numero entre os 3 é: {menor3n}")
    
'''





'''

#Exercício 1
nm1 = random.randint (1, 10)
nm2 = random.randint (1, 10)

lista = [nm1, nm2]
print ("Exercício 01")
print(lista)
lista.sort(reverse = True)
print (lista [0])
print()

#Exercício 2 
nm3 = random.randint (1, 10)

lista = [nm1, nm2, nm3]
print ("Exercício 02")
print(lista)
lista.sort()
print (lista [0])

'''