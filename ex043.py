p = float(input("Qual o seu peso: (KG) "))
a = float(input("Qual a sua altura: "))
imc = p / a**2
print(f"Você está com o IMC = {imc:.1f}")
if imc < 18.5:
    print("\033[33mVocê está abaixo do peso ideal.\033[m")
elif imc >= 18.5 and imc < 25:
    print("\033[32mVocê está no peso ideal.\033[m")
elif imc >= 25 and imc < 30:
    print("\033[30mVocê está em sobrepeso.\033[m")
elif imc >= 30 and imc <= 40:
    print("\033[34mVocê está com obesidade.\033[m")
elif imc > 40:
    print("\033[31mVocê está com obesidade mórbida.\033[m")

    