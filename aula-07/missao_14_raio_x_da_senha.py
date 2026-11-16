nome = input("Seu nome? ")
senha = input("Sua senha? ")

print(f"Tamanho da senha: {len(senha)}")
print(f"Contém o nome? {nome.lower() in senha.lower()}")
print(f'Contém "123"? {"123" in senha}')
