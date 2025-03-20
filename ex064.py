soma = 0
cont = 0
n = int(input("Digite um número [999 para parar]: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número [999 para parar]: "))
print(f"A soma desses {cont} números é  {soma}.")
