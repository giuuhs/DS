import os
os.system("cls")


#Soma numero ate digitar 0
soma = 0

while True: 
    n = int(input("Numero:"))
    soma += n
    if n==0:
        break

    print("Soma:", soma)

