n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("""
        opções:
        [ 1 ] somar os números
        [ 2 ] multiplicar
        [ 3 ] informar o maior
        [ 4 ] novos números
        [ 5 ] sair do programa
""")
    opcao = int(input("Qual a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma de {n1} com {n2} é {soma}.")
    elif opcao == 2:
        prod = n1 * n2
        print(f"O produto de {n1} e {n2} é {prod}.")
    elif opcao == 3:
        if n2 > n1:
            maior = n2
            print(f"O maior é {maior}")
        elif n1 > n2:
            maior = n1
            print(f"O maior é {maior}")
        else:
            print("Eles são iguais.")
    elif opcao == 4:
        print("Informe novos números: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Fim do programa, volte sempre.")
    else:
        print("Opção inválida, tente novamente.")


    
        