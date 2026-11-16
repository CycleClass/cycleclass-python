nome = input("Nome? ")
sobrenome = input("Sobrenome? ")

nome_completo = f"{nome} {sobrenome}"
iniciais = f"{nome[0]}{sobrenome[0]}"

print(f"CRACHÁ: {nome_completo.upper()}")
print(f"Primeiro nome: {nome}")
print(f"Iniciais: {iniciais.upper()}")
