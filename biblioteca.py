'''
DEFINIÇÃO: Verifica se uma string é float
PARÂMETROS:
    v: string
RETORNO:
    Booleano
'''
def isfloat(v: str) -> bool:
    if v[0] == '-' or v[0] == '+':
        v = v.replace("-",'',1)
    v = v.replace(".","",1)
    return v.isdigit()

def isint(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] in "+-" or s[0] in digito: 
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False
    
    return valido

# Parâmetros default
def saudacao(usuario: str = "Edson", hora: int = 8) -> None:
    if hora < 12:
        turno = "Bom dia"
    elif hora < 18:
        turno = "Boa Tarde"
    else:
        turno = "Boa Noite"
    
    print(f"{usuario}, {turno}!\nSeja bem-vindo!")



import os
os.system("cls")
# Parametro *args
def soma_numeros(*args) -> float:
    soma = 0
    for num in args:
        soma += num
    return soma

print(soma_numeros(5,9,9,9))


"""
EXERCICIOS:
1. Verificar se a placa (antiga ou nova) de um carro é válida, 
Retornando: True ou False 
Quantos parametros? 1 - str
Tipo valor retornado? bool

    Antiga: LLL9999
    Nova:   LLL9L99

Exemplos:
4535365  - False
rrrr5555 - False
ede5555  - True
fly5k44  - True
dlr4l999 - False
"""
