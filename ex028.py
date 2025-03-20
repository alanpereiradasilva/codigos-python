from random import randint
c = randint(0, 5)
n = int(input("Digite um número inteiro: "))
if n == c:
    print(f"Parabéns, Você venceu! eu também pensei em {c}")
else:
    print(f"Você perdeu! eu pensei em {c} e não em {n}")