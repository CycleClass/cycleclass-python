# Missão 09 - Conta do café
# Ler o produto, o preço (float) e a quantidade (int)
# e mostrar o total a pagar, usando uma f-string.

produto = input("Produto? ")
preco = float(input("Preço? "))
quantidade = int(input("Quantidade? "))

total = preco * quantidade

print(f"{quantidade} x {produto}: R$ {total}")
