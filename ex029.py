v = int(input("Qual a velocidade atual do carro? "))
if v > 80:
    m = (v - 80) * 7 
    print("Multado! você excedeu o limite permitido que é 80 KM/H.")
    print(f"Você deve pagar uma multa de {m:.2f} R$.")
    print("Tenha um bom dia, dirija com segurança.")
else:
    print("Tenha um bom dia, dirija com segurança.")