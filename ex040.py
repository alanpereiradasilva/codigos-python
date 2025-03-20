n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
media = (n1 + n2) / 2
if media >= 60:
    print("\033[32mO aluno está aprovado.\033[m")
elif media >= 40 and media < 60:
    print("\033[33mO aluno está em recuperação.\033[m")
else:
    print("\033[31mO aluno está reprovado.\033[m")