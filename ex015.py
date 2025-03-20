dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos KM ele percorreu? "))
total = dias*60+km*0.15
print(f"O total a pagar é de {total:.2f} R$")