import math
a = int(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(a))
print(f"O ângulo de {a}° tem o SENO de {seno:.2f}")
cosseno = math.cos(math.radians(a))
print(f"O ângulo de {a}° tem o COSSENO de {cosseno:.2f}")
tangente = math.tan(math.radians(a))
print(f"O ângulo de {a}° tem a TANGENTE de {tangente:.2f}")
