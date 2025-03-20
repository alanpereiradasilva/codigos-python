n = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para convenção:
      [ 1 ] converter para binário
      [ 2 ] converter para octal
      [ 3 ] converter para hexadecimal
""")
opcao = int(input("Qual a sua opção? "))
if opcao == 1:
    print(f"{n} convertido para binário é igual a {bin(n)[2:]}.")
elif opcao == 2:
    print(f"{n} convertido para octal é igual a {oct(n)[2:]}.")
elif opcao == 3:
    print(f"{n} convertido para hexagonal é igual a {hex(n)[2:]}.")
else:
    print("Opção inválida, tente novamente.")