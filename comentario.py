#Giulia de Souza Resende Santos 2ai
#Biana Pereira Cunha 2ai


import os 
os.system('cls')

comentarios = [" O produto é excelente e muito bom!",
    " Péssimo atendimento. Horrível!",
    " A entrega foi ruim, mas o produto é bom",
    " Ótimo custo-benefício",
    " Não gostei, é horrível"
]

irrelevantes = ['e', 'o', 'a', 'os', 'as', 'de', 'da', 'do', 'é', 'foi', 'um', 'uma', 'em','mas']

positivas = ['bom', 'ótimo', 'otimo', 'excelente', 'maravilhoso']

negativas = ["ruim", "péssimo", "péssima", "horrível", "horrivel", "terrível"]

def analisar_comentarios(lista):
    positivos = 0
    negativos = 0
    total_palavras = 0

    for comentario in lista:
        palavras = comentario.lower().replace("!", "").replace(".", "").split()
        for palavra in palavras:
            if palavra not in irrelevantes:
                total_palavras += 1
                if palavra in positivas:
                    positivos += 1
                elif palavra in negativas:
                    negativos += 1

    print("\n===== RESULTADO DA ANÁLISE =====")
    print(f"Comentários positivos: {positivos}")
    print(f"Comentários negativos: {negativos}")
    print(f"Total de palavras úteis analisadas: {total_palavras}")


# PROGRAMA PRINCIPAL (Menu)

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Exibir comentários")
        print("2. Adicionar novo comentário")
        print("3. Analisar comentários")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nCOMENTÁRIOS:")
            for i, c in enumerate(comentarios, 1):
                print(f"{i}. {c}")

        elif opcao == "2":
            novo_comentario = input("Digite o novo comentário: ")
            comentarios.append(novo_comentario)
            print("Comentário adicionado com sucesso!")

        elif opcao == "3":
            analisar_comentarios(comentarios)

        elif opcao == "4":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    menu()

