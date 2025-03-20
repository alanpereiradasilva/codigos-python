n = int(input("Digite um número: "))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
print(f"O número {n} foi divísivel {tot} vezes.")
if tot == 2:
    print("Por isso ele é primo.")
else:
    print("Por isso ele não é primo.")