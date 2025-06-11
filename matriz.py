import os
os.system("cls")

def exibe_matriz(m: list) -> None:
    # Exibindo a matriz
    print("Matriz: ")
    for linha in m:
        for elemento in linha:
            print(elemento, end=' ')
        print()


# Definindo uma matriz 2 x 3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
]

print(matriz)



print()
# Exibindo a matriz forma tradicional
for l in range (2):
    for c in range (3):
        print(f"{matriz[l][c]}", end = " ")
    print()

os.system("cls")
matriz =[]

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"[{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a matriz
exibe_matriz(matriz)

'''
EXERCICIOS:

[onde você ler rotina, faça uma função/procedimento]

1. Faça uma rotina que peça ao usuário a digitação dos elementos de uma matriz 3 x 4.
(Ela servirá como base para os próximos exercicios)
[[45, 76, 23, 45], [22, 21, 87, 90], [12, 19, 39, 37]]

2. Faça uma rotina que exiba o conteúdo da matriz.
  0  1  2  3
0 45 76 23 45
1 22 21 87 90
2 12 19 39 37

3. Faça uma rotina que exiba somente os elementos pares.
76 22 90 12

4. Faça uma rotina que conte quantos elementos ímpares tem na matriz.
Impares: 8

5. Faça uma rotina que peça um numero ao usuário e, caso o encontre na matriz, retorne a linha
e coluna onde ele se encontra, caso contrário retorne False (trate o problema do no programa principal)
Valor: 87
[1,2]

Valor: 99
Não existe

6. Faça uma rotina que passe a matriz por parâmetro e copie em uma segunda matriz 0 ou 1 nos elemntos
caso o da primeira seja par ou impar, respectivamente.
Matriz 1
45 76 23 45
22 21 87 90
12 19 39 37

Matriz 2
1 0 1 1
0 1 1 0
0 1 1 1

'''