import os
os.system("cls")

#         0   1   2   3   4   5
vetor = [45, 59, 66, 32, 45, 44]
vetor[6] = int(input("Digite um valor:"))
print(vetor[6])

# Exibe o vetor integralmente
print(vetor)

# Exibe as posições pelo índice
for i in range(0, len(vetor),1): # len() retorna quantos elementos temos no vetor
    print(f"Vetor[{i}] = {vetor[i]}")

print()
for elem in vetor:
    print(elem)

print()
#         0   1   2   3   4   5
vetor = [45, 59, 66, 32, 45, 44]

for ind, elem in enumerate(vetor):
    print(f"Vetor[{ind}] = {elem}")

"""
Exercícios
1. Somar os elementos do vetor
2. Calcular a média
3. Verificar quantos elementos são acima da média
"""
# 1. Somar os elementos do vetor
soma = 0
for elem in vetor:
    soma += elem
print(f"Soma = {soma}")

# 2. Calcular a média
media = soma / len(vetor)
print(f"Media = {media}")

# 3. Verificar quantos elementos são acima da média
cont = 0
for elem in vetor:
    if elem > media:
        cont += 1
print(f"Acima da média = {cont}")