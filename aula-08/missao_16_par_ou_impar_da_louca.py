# Missão 16 - Par ou ímpar da louça
# Duas pessoas dizem um número cada. Se a soma for par, a primeira lava
# a louça; se for ímpar, a segunda.

n1 = int(input("Número da primeira pessoa? "))
n2 = int(input("Número da segunda pessoa? "))

soma = n1 + n2

if soma % 2 == 0:
    print(f"Soma {soma}: par.")
    print("A primeira pessoa lava a louça.")
else:
    print(f"Soma {soma}: ímpar.")
    print("A segunda pessoa lava a louça.")
