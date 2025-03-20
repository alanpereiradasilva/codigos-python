casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao}.")
if prestacao > 0.3 * salario:
    print("Empréstimo negado!")
else:
    print("Empréstimo aceito!")
