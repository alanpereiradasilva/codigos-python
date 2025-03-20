soma = 0
cont = 0
while True:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        soma += n
        cont += 1
    else:
        break
print(f"A soma desse {cont} números é {soma}.")