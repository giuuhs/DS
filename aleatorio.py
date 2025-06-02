
#sortear  numeros

import time
import random
import os
os.system("cls")
a = 0
qnt = 0

while True: 
    print(" MENU\n 0 - SAIR\n 1 - Sortear o numero\n 2 - Jogar\n 3 - Estatistica\n Escolha: ")
    nm= float(input("O que quer acessar? "))
    if nm == 0:
        break
# 1 ________________________
    elif nm == 1:
        sorteado = random.randint (1, 10)
        print("Numero Sorteado")
        time.sleep(1)
# 2 ________________________
    elif nm == 2:
        qnt = qnt + 1
        for cont in range (0, 3, 1):
            n = float(input("De seu palpite: "))
            if n == sorteado: 
                print("Acertou!!!")
                time.sleep(1)
                print("Fim de jogo")
                a = a + 1
                break

            elif n < sorteado: 
                print("Errou! O numero sorteado está acima de N")
                a = a + 1
                
            elif n > sorteado: 
                print("Errou! O numero sorteado está abaixo de N")
                a = a + 1
            else:
                print("Fim de jogo")
                a = a + 1
                break
# 3 ________________________

    elif nm == 3:
        print(f"Voce  teve {a} tentativas")
        print(f"Voce  jogou {qnt} vezes")

        input()



