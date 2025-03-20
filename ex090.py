aluno = {}
aluno['nome'] = str(input("Nome do aluno: "))
aluno['média'] = int(input(f"Média de {aluno['nome']}: "))
if aluno['média'] >= 60:
    aluno['situação'] = 'APROVADO'
elif aluno['média'] >= 40 and aluno['média'] < 60:
    aluno['situação'] = 'RECUPERAÇÃO'
elif aluno['média'] < 40:
    aluno['situação'] = 'REPROVADO'
for k, v in aluno.items():
    print(f"{k} é igual a {v}.")
