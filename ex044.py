preco = float(input("Qual o preço do produto? "))
print("""Opções de pagamento:
[ 1 ] À vista em dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] 2x vezes no cartão.
[ 4 ] 3x ou mais no cartão.""")
opçao = int(input("Qual a sua opção? "))
if opçao == 1:
    desc = preco - preco * 0.1
    print(f"O preço de {preco:.2f} R$ com desconto fica {desc:.2f} R$ em dinheiro ou cheque.")
elif opçao == 2:
    desc = preco - preco * 0.05
    print(f"O preço de {preco:.2f} R$ com desconto fica {desc:.2f} R$ no cartão.")
elif opçao == 3:
    parcela = preco / 2
    print(f"O preço de {preco:.2f} R$ ficará parcelado em 2x de {parcela:.2f} R$ sem juros.")
elif opçao == 4:
    juros = preco + preco * 0.2
    parcelas = int(input("Quantas parcelas? "))
    parcela = juros / parcelas
    print(f"O preço de {preco:.2f} R$ ficará parcelado em {parcelas}x de  {parcela:.2f} R$ com juros.")
else:
    print("Opção inválida. Tente novamente.")
