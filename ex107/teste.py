import moeda
p = float(int(input("Digite o preço: R$")))
print(f"A metade de R${p} é {moeda.metade(p)}")
print(f"O dobro de R${p} é {moeda.dobro(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10)}")
print(f"Diminuindo 10%, temos {moeda.diminuir(p, 10)}")
