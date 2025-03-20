matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para [{l}, {c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] %2 == 0:
            spar += matriz[l][c]
for l in range(0, 3):
    if c == 2:
        scol += matriz[l][c]
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[l][c] > mai:
        mai = matriz[1][c]
print(f"A soma dos valores pares é {spar}.")
print(f"A soma dos valores da terceira coluna é {scol}.")
print(f"O maior valor da segunda linha é {mai}.")
