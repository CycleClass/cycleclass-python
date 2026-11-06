# Missão 08 - Máquina do tempo
# Ler a idade e mostrar a idade daqui a 1, 5 e 10 anos,
# e em que ano isso será.

idade = int(input("Idade? "))
ano = 2026  # o ano de hoje, escrito direto no programa

idade_1 = idade + 1
idade_5 = idade + 5
idade_10 = idade + 10
ano_1 = ano + 1
ano_5 = ano + 5
ano_10 = ano + 10

print(f"Em {ano_1} você terá {idade_1} anos.")
print(f"Em {ano_5} você terá {idade_5} anos.")
print(f"Em {ano_10} você terá {idade_10} anos.")
