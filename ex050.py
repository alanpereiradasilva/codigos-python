soma_pares = 0
cont_pares = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c}º número: "))
    if n %2 == 0:
        soma_pares += n
        cont_pares += 1
print(f"A soma dos {cont_pares} números pares foi {soma_pares}.")