print("CADASTRO DE PESSOAS.")
adultos = 0
homens = 0
moças = 0
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        adultos += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        moças += 1
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar?[S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Temos {adultos} pessoas com mais de 18.")
print(f"Temos {homens} homens cadastrados.")
print(f"E temos {moças} mulheres com menos de 20 anos.")
