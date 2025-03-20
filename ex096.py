def calcular_area(larg, comp):
    area = larg * comp
    print(f"A área de um terreno {larg}x{comp} é de {area:.2f}M².")


# Programa principal
print('Controle de terrenos')
print('-' * 20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
calcular_area(l, c)
