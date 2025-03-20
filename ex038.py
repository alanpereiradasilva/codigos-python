n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
   print(f"Primeiro número é maior.")
elif n2 > n1:
    print("Segundo número é maior.")
else:
    print("\033[32mEles são iguais.\033[m")