from random import randint
comp = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    n = int(input("Qual o seu palpite? "))
    palpite += 1
    if n == comp:
        acertou = True
    else:
        if n < comp:
            print("Mais... Tente novamente.")
        elif n > comp:
            print("Menos... Tente novamente.")
print(f"Parabéns, você acertou com {palpite} tentativas.")
