print("Banco do Alan!")
valor = int(input("Quanto você quer sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f"Total de {totced} cédulas de {ced:.2f} R$.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("Volte sempre ao Banco do Alan, tenha um bom dia.")

