co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjascente: "))
hip = co**2 + ca**2
hi = hip**(1/2)
print(f"A hipotenusa vai medir {hi:.2f}")
