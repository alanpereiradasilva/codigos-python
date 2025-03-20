from random import randint
from time import sleep
itens = ("pedra", "papel", "tesoura")
comp = randint(0, 2)
jog = int(input("Qual a sua jogada? "))
print("JO")
sleep(1.5)
print("KEN")
sleep(1.5)
print("PO")
print(f"Computador jogou {itens[comp]}")
print(f"Jogador jogou {itens[jog]}")
if comp == 0:
    if jog == 0:
        print("Empate.")
    elif jog == 1:
        print("Jogador venceu.")
    elif jog == 2:
        print("Computador venceu.")
    else:
        print("Jogada inválida.")
elif comp == 1:
    if jog == 0:
        print("Computador venceu.")
    elif jog == 1:
        print("Empate.")
    elif jog == 2:
        print("Jogador venceu.")
    else:
        print("Jogada inválida.")
elif comp == 2:
    if jog == 0:
        print("Jogador venceu.")
    elif jog == 1:
        print("Computador venceu.")
    elif jog == 2:
        print("Empate.")
    else:
        print("Jogada inválida.")