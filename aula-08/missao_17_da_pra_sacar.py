# Missão 17 - Dá pra sacar?
# Ler o saldo e o valor do saque e dizer se é possível e quanto sobra.

saldo = float(input("Saldo? "))
saque = float(input("Valor do saque? "))

if saque <= saldo:
    sobra = saldo - saque
    print("Saque liberado!")
    print(f"Saldo restante: R$ {round(sobra, 2)}")
else:
    print("Saque negado: saldo insuficiente.")
