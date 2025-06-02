import os
os.system("cls")

salario = float(input("Digite your salario: "))
if salario < 1518.00:
    aliquota= salario * 0.075 
    print(f"O valor a ser pago é de: {aliquota}")

elif salario > 1518.01 or salario < 2793.88:
    aliquota= salario * 0.09 
    print(f"O valor a ser pago é de: {aliquota}")

elif salario > 2793.89 or salario < 4190.83:
    aliquota= salario * 0.12 
    print(f"O valor a ser pago é de: {aliquota}")

elif salario > 4190.84 or salario < 8157.41:
    aliquota= salario * 0.14 
    print(f"O valor a ser pago é de: {aliquota}")

elif salario > 8157.42:
    aliquota= salario + 951.62 
    print(f"O valor a ser pago é de: {aliquota}")
