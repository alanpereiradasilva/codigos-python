# Meu código
lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    resp = str(input("Quer continuar? [S/N]: "))
    if resp in "Nn":
        break
    
    if n %2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f"A lista completa é {lista}.")
print(f"A lista de pares é {lista_par}.")
print(f"A lista de impares é {lista_impar}.")

# Código do Gustavo Guanabara
# num = list()
# pares = list()
# ímpares = list()
# while True:
#     num.append(int(input("Digite um número: ")))
#     resp = str(input("Quer continuar? [S/N] "))
#     if resp in "Nn":
#         break
# for i, v in enumerate(num):
#     if v %2 == 0:
#         pares.append(v)
#     elif v %2 == 1:
#         ímpares.append(v)
# print(f"Lista completa {num}.")
# print(f"Lista dos pares {pares}.")
# print(f"Lista dos ímpares {ímpares}.")
