from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    n = int(input(f"Em que ano nasceu a {c}º pessoa? "))
    idade = ano - n
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo temos {maior} maiores de idade.")
print(f"E temos {menor} menores de idade.")