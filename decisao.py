# Operadores relacionais
# > >= < <= != ==

# Operadores lógicos
# not [!] and [&&] or [||]

#errado

idade = 20
if (idade >= 18){
    print("maior de idade");
}
else{
    print("menor de idade");
}

#certo

import os
os.system("cls")

idade = 20
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")


# use a porra da tabulação

import  os
os.system ("cls")
# decisão simples: if
x = -5
if x < 0:
    x = -x
    print(x)

import  os
os.system ("cls")
#decisão encadeada: if elif
x = -5
if x < 0:
    x = -x
elif x > 0:
    print (x)


import  os
os.system ("cls")
#decisão encadeada: if elif
x = -5
if x < 0:
    print("Negativo")
elif x > 0:
    print("Positivo")
else: 
    print("Nulo")

x = 50
if x < 0 :
    print("positivo")
else: 
    print ("nulo")


    """ 
    EXERCÍCIOS
    1. Pesquisar tabela INSS 2025 e fazer um programa que pegue o salário de um funcionário
    e informe quanto ele pagará de INSS.
    2. Pesquisa a tabela de IMPOSTO DE RENDA 2025 e fazer um programa que pegue
    o salário de um funionário e informe o quanto ele pagará de IMPOSTO DE RENDA.
    3. Dado o saláro de um funcionário, calcular os impostos acima, exibindo os dados da seguinte forma:
    -----------------------------------------------------------------------------------------------------
    Salário bruto: R$  9999999.99
    INSS: R$  9999999.99
    IR: R$  9999999.99
    Salário líquido: R$  9999999.99
    -----------------------------------------------------------------------------------------------------
    """



