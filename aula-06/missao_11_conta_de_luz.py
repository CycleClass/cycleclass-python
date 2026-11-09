# Missão 11 - Conta de luz
# Calcular a conta a partir dos kWh consumidos, da tarifa e da taxa fixa,
# com duas casas decimais (round).

kwh = int(input("Consumo em kWh? "))
tarifa = float(input("Tarifa por kWh? "))
taxa = float(input("Taxa fixa? "))

total = kwh * tarifa + taxa

print(f"Total da conta: R$ {round(total, 2)}")
