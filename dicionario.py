import os
os.system("cls")

#Dicionario vazio
dicionarinho = dict()
dicionarinho = ()
print(dicionarinho)

#Sintaxe
chavinho = {
    "chave1": "valor",
    "nome": "Yuri",
    "curso": "corinthians",
    "idade": 19 
}
print(chavinho)
print(chavinho["chave1"])
'''
#Modificando valor no dicionario
chavinho["idade"] = 30
print(chavinho)
chavinho["idade"] = int(input("Idade: "))
print(chavinho)
'''

#Adicinando novas keys
chavinho["nota"] = 8.7

#Removendo itens
chavinho.pop("chave1")
del chavinho["idade"]
print(chavinho)

#O del apaga/mata onde ele exclui onde nem pode ser exibido
del chavinho

#Metodos dicionario
"""
get retorna um valor


"""
