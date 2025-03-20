print("\033[32mGerador de P.A.\033[m")
p = int(input("Primeiro termo: "))
r = int(input("Razão da P.A: "))
t = p
cont = 1
while cont <= 10:
    print(f"{t} -> ", end='')
    t += r
    cont += 1
print("Fim")
 