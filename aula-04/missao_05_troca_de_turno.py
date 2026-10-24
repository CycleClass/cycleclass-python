# Missão 05 - Troca de turno
# Trocar os valores de manha e noite de dois jeitos.

# Jeito 1: com uma variável auxiliar (como na Lógica)
manha = "Ana"
noite = "Bia"
print("Antes:  manhã =", manha, "| noite =", noite)

aux = manha      # guarda a Ana numa terceira caixa
manha = noite    # a manhã recebe a Bia
noite = aux      # a noite recebe a Ana, que estava guardada

print("Depois: manhã =", manha, "| noite =", noite)

# Jeito 2: o jeito Python, numa linha só
manha = "Ana"
noite = "Bia"
manha, noite = noite, manha
print("Jeito 2: manhã =", manha, "| noite =", noite)
