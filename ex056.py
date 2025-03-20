soma_idade = 0
media = 0
maior_idade_homem = 0
nome_homem = ''
novinhas = 0
for c in range(1, 5):
    print(f"-----{c}º Pessoa-----")
    nome = str(input("Nome: ")).strip()
    idade = int(input(f"Idade de {nome}: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    if c == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_homem = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem = nome
    if idade < 20 and sexo in "Ff":
        novinhas += 1
media = soma_idade / 4
print(f"A média de idade desse grupo é de {media} anos.")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem}.")
print(f"Ao todo temos {novinhas} mulheres  com menos de 20 anos.")