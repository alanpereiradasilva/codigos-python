from random import randint
from time import sleep
lista = []
jogos = []
quant = int(input("Quantos jogos você quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"Sorteando {quant} jogos:")
for i, v in enumerate(jogos):
    print(f"{i+1}º jogo: {v}")
    sleep(1)
print("<<< Boa sorte! >>>")

        
