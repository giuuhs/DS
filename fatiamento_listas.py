import os
os.system("cls")

# Fatiamento
#           0   1   2   3   4   5   6   7   8   9   
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#          -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
print(numeros)
print(numeros[4])
print(numeros[-3])
n = numeros[3:7]
print(n)
print(numeros[2:9:3])
print(numeros[9:2:-2])
print(numeros[-3:])
print(numeros[-3:-1])
print(numeros[::-1])

# Tupla
lista = [1,2,3,4,5] # list()
tupla = (3,4,5,6,7) # tuple()
print(tupla[3])
print(type(lista), type(tupla))
x = list(tupla)
print(type(x))

# Fatiamento de string
frase = "Agora veremos como funciona o fatiamento de strings"
print(frase)
print(frase[2])
print(frase[2:10])
print(frase[::3])
print(frase[::-1])

# metodos para strings
#        012345678901234567890123456789012345678901234567890
frase = "Agora veremos como funciona o fatiamento de strings"
# find(substring, inicio,fim) -> busca uma substring
print(frase.find("como"))
print(frase.find("x")) # -1 não existe
print(frase.find("a")) 
print(frase.find("a",10,30)) 

# join(lista_de_strings) -> junta uma lista de strings em uma string
os.system("cls")
lista_nome = ["Edson", "de", "Oliveira"]
print(lista_nome)
str_nome = " ".join(lista_nome)
print(str_nome)

# split(str_separadora) -> contrário de join
os.system("cls")
nome = "Edson de Oliveira"
print(nome)
print(nome.split())
print(nome.split(" "))
print(nome.split('e'))
print(nome.split('de'))

# replace(procura, troca, cont)
os.system("cls")
nome = "edson de Oliveira"
print(nome.replace('e','E'))
print(nome.replace('de','minha nossa nossa nossa'))
print(nome.replace('e','E',2))

# strip() -> elimina os espaços das extremidades
os.system("cls")
texto = "     elimina os espaços     "
print(texto)
print(texto.strip())

# operador in
os.system("cls")
x = 'E'
if x in 'Edson':
    print(f"tem {x}")
else:
    print(f"não tem {x}")

numeros = [45,34,23,76,65]
if 555 in numeros:
    print(f"está ")
else:
    print(f"não está ")

# Exercicio
'''
1. crie a função: vogal_maiuscula(string) -> str:




2. cria a função: isfloat(string) -> boolean:
    resp = isfloat("edson") # False
    resp = isfloat("45.78") # True
    resp = isfloat("65") # True
    resp = isfloat("-98") # True
    resp = isfloat("234,67") # False
    resp = isfloat("+22.78") # True
    resp = isfloat("44.777.88") # False

'''




