frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0

for letra in frase:
    if letra.isalpha():
        if letra.lower() in "aeiou":
            vogais += 1
        else:
            consoantes += 1

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
