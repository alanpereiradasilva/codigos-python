s = float(input("Digite o salário do funcionário: "))
if s > 1250:
    n_s = s + s * 0.1
else:
    n_s = s + s * 0.2
print(f"Quem ganhava {s:.2f}R$ passa a ganhar {n_s}R$ agora.")