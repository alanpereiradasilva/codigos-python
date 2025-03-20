total = 0
totmil = 0
menor = 0
cont = 0
barato = ''
while True:
    nome =str(input("Qual o nome do produto? ")).strip()
    preço = float(input("Preço do produto: "))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = " "
    if resp not in "SN":
        resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp == "N":
        break
print(f"O preço total em compras foi de R${total:.2f}.")
print(f"Ao todo foram {totmil} itens com preços maiores que 1000 R$.")
print(f"O produto mais barato foi o(a) {barato} que custa {menor:.2f}R$ ")
