from random import randint
v = 0
while True:
    jog = int(input("Diga um valor: "))
    comp = randint(0, 10)
    total = jog + comp
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Impar [P/i]: ")).strip().upper()[0]
    print(f"Você jogou {jog} e o computador {comp}. Total de {total}.")
    print("Deu par." if total %2 == 0 else "Deu ímpar.")
    if tipo == 'P':
        if total %2 == 0:
            print("Você venceu.")
            v += 1
        else:
            print("Você perdeu.")
            break
    elif tipo == 'I':
        if total %2 == 1:
            print("Você venceu.")
            v += 1
        else:
            print("Você perdeu.")
            break
    print("Vamos jogar novamente...")
print(f"Você venceu {v} seguidas.")
