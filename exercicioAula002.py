import os
os.system("cls")

didi = {
    "Nome" : "Timao",
    "Idade" : 115,
    "Nota": 10
}

def acrescentar_campo (didi: dict) -> dict:
    didi["Nota"] = 9
    return didi

def menu():
    escolha = int(input("""
    1 - Acrescentar campo
    2 - Remover campo
    3 - Editar o registro
        (a) Nome
        (b) Idade
        (c) Nota
    4 - Mostrar o registro
    0 - SAIR
    Escolha a sua opção:
"""))
    
    if escolha == 1:
        acrescentar_campo(didi)
    elif escolha == 2:
        print("vsfd")

menu()    

    
