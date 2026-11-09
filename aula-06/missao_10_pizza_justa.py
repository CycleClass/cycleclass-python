# Missão 10 - Pizza justa
# Ler quantas pessoas vão comer, quantas fatias cada uma come
# e quantas fatias tem cada pizza. Mostrar quantas pizzas inteiras
# dá e quantas fatias sobram (// e %).

pessoas = int(input("Quantas pessoas? "))
fatias_cada = int(input("Fatias por pessoa? "))
fatias_pizza = int(input("Fatias por pizza? "))

total = pessoas * fatias_cada

inteiras = total // fatias_pizza
sobram = total % fatias_pizza

print(f"Total de fatias: {total}")
print(f"Pizzas inteiras: {inteiras}")
print(f"Fatias que sobram: {sobram}")
