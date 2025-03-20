primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end='')
        termo += razão
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"A progressão foi finalizada com {total} termos mostrados.")