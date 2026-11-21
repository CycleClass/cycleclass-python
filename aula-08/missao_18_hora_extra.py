# Missão 18 - Hora extra
# Ler as horas trabalhadas na semana. Acima de 44 horas, calcular as horas
# extras e o valor com 50% a mais.

horas = int(input("Horas trabalhadas na semana? "))
valor_hora = float(input("Valor da hora? "))

if horas > 44:
    extras = horas - 44
else:
    extras = 0

normais = horas - extras
total = normais * valor_hora + extras * valor_hora * 1.5

print(f"Horas extras: {extras}")
print(f"Total a receber: R$ {round(total, 2)}")
