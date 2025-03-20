from datetime import date
atual = date.today().year
nasc = int(input("Em que ano você nasceu? "))
idade = atual - nasc
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Sua categoria é mirim.")
elif idade <= 14:
    print("Sua categoria é infantil.")
elif idade <= 19:
    print("Sua categoria é junior.")
elif idade <= 25:
    print("Sua categoria é senior.")
else:
    print("Sua categoria é master.")