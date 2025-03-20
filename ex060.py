n = int(input("Digite um número para ver seu fatorial: "))
c = n
f = 1
print(f"Calculando {n}! = ", end='')
while c >= 1:
    print(f"{c}", end='')
    f *= c
    c -= 1
    print(" x " if c >= 1 else " = ", end='')
print(f"{f}.")

