palavra = input("Digite uma palavra: ").strip()

invertida = palavra[::-1]

if palavra.lower() == invertida.lower():
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
