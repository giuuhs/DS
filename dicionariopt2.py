import os
os.system("cls")

#Metodos
aluno = {
'aluno_do_pai' : 'edson',
'idade' : 14,
'curso' : 'DS', 
}

#metodos
print(aluno)

#key() - cria lista com as chaves
print(aluno.keys())

#values() - cria uma lista com valores
print(aluno.values())

#items() - cria uma lista com ois items do dicionario
print(aluno.items())

# campos     k -> keys   capitalize() -> primeira letra em maiuscula
print()
for k in aluno.keys():
    print(k.capitalize()) 
print(aluno.keys())

# valores 
print()
for k, v in aluno.items():
    print(f"Campo: {k:15} -> Valor: {v}")
print(aluno.items())

#update() -> ele modifica apenas os que voce quiser alterar
aluno.update({"nome_do_pai": "Manoel Gomes", "idade": 98})
print(aluno)

#clear () -> ele apaga as chaves e os values
aluno.clear()