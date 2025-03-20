def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    para n: Uma ou mais notas dos alunos (aceita várias).
    para sit: Valor opcional, indicando se deve ou não adicionar a situação.
    return: dicionário com várias informações sobre a turma."""
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5 and r['media'] < 7:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
