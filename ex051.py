primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end=' -> ')
print("Acabou.")