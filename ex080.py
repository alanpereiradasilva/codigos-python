lista = []
for c in range(0, 5):
    n = int(input(f"Digite o {c+1}º número: "))
    if c == 0 or n > lista[len(lista)-1]: # lista[-1]
        lista.append(n)
        print("Número adicionado no final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Número adicionado na posição {pos}")
                break
            pos += 1
print(f"Os valores digitados em ordem foram {lista}.")
