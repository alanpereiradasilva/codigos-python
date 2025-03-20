vi = float(input("Qual a distância da sua viagem? "))
if vi <= 200:
    p = vi * 0.5
else:
    p = vi * 0.45

print(f"Você está prestes a começar uma viagem de {vi} KM.")
print(f"E o preço da sua passagem é {p:.2f} R$.")
