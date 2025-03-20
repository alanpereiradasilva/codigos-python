resp = "S"
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    quant += 1
    if quant == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
media = soma / quant
print(f"Você digitou {quant} números e a média foi {media}")
print(f"O maior número digitado é {maior} e o menor foi {menor}")
