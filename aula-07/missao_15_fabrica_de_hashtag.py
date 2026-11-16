frase = input("Frase? ")

texto = frase.strip().lower().replace(" ", "")
hashtag = f"#{texto}"

print(hashtag)
