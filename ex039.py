from datetime import date
atual = date.today().year
nasc = int(input("Em que ano você nasceu? "))
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
if idade == 18:    
    print("\033[33mVocê tem que se alistar IMEDIATAMENTE!\033[m")
elif idade < 18:
    saldo = 18 - idade
    print(f"\033[32mAinda falta(m) {saldo} ano(s) para o alistamento.\033[m")
elif idade > 18:
    saldo = idade - 18
    print(f"\033[31mVocê já deveria ter se alistado há {saldo} ano(s).\033[m")
