# Missão 12 (desafio) - Bhaskara, parte 1
# Calcular o delta e as duas raízes de uma equação do 2º grau,
# supondo delta >= 0.

a = float(input("a? "))
b = float(input("b? "))
c = float(input("c? "))

delta = b ** 2 - 4 * a * c

x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print(f"Delta: {delta}")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
