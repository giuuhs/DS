# %% [markdown]
# #### Subalgoritmos
# ##### Função - Executa uma rotina que retorna um valor
# ##### Procedimento - Executa uma rotina que NÃO retorna  valor

# %%
valor = 6

# %% [markdown]
# <b>Sintaxe:</b>
# ```python
# def nome_subalgoritmo(parâmetros) -> retorno:
#     corpo do subalgoritmo
#     return valor # caso seja função
#     

# %%
# Exibir uma saudacao - PROCEDIMENTO

# Procedimento
def saudacao() -> None:
    print("Bom dia aluno")

# Chamada do procedimento
saudacao()



# %%
# Exibir uma saudacao com parâmetro- PROCEDIMENTO

# Procedimento
def saudacao2(aluno: str) -> None:
    print(f"Bom dia {aluno}")

# Chamada do procedimento
saudacao2("Edson")

# %%
# Exibir uma saudacao com 2 parâmetros- PROCEDIMENTO

# Procedimento
def saudacao3(aluno: str, hora: int) -> None:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    
    print(f"{msg} {aluno}")

# Chamada do procedimento
saudacao3("Maria", 19)

# %% [markdown]
# #### Função
# <b>Sintaxe:</b>
# ```python
# def nome_subalgoritmo(parâmetros) -> retorno:
#     corpo do subalgoritmo
#     return valor # caso seja função

# %%
def soma2numeros(n1: float, n2: float) -> float:
    resultado = n1 + n2
    return resultado # return só em função

x = soma2numeros(56,88)
print(x)
print(soma2numeros(10,20))
print(valor)


