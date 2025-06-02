import os
os.system("cls")

nome = "edson oliveira"
idade = 50 
salario = 45987.85

#forma 1 - clássica (separa dados de qualquer tipo)
print(nome, idade, salario)
print("nome: ", nome, "\nidade: ", idade, "\nsalario: ", salario)
print("nome: ", nome, "\nidade: ", idade, "\nsalario: ", salario)

#Forma 2 - Utilizando a funçaõ format

print("\nNome : {0}\nIdade: {1}\nSalário: {2}".format(nome,idade, salario))
print("\nNome : {n}\nIdade: {i:05d}\nSalário: {s:14.2f}".format(n=nome, i=idade, s=salario))

#Forma 3 - Utilizando o fprint

print(f"\nNome : {nome}\nIdade: {idade}\nSalário: {salario}")
print(f"\nNome : {nome}\nIdade: {idade}\nSalário: {salario}")

#Forma 4 - Utilizando triple quotes """

print(f"Nome : {nome}", end = ".")
print(f"Idade : {idade}", end = ".")
print(f"Salarios : {salario}", end = ".")

print(f"""
Nome: {nome}
Idade: {idade}
Salario: {salario}
""")