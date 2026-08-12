senha = input("Digite uma senha: ")

tem_letra = False
tem_numero = False

for caractere in senha:
    if caractere.isalpha():
        tem_letra = True
    if caractere.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_letra and tem_numero:
    print("Senha forte!")
else:
    print("Senha fraca.")
