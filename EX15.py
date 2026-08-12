placa = input("Digite a placa: ").strip()

if len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric():
    print("Placa válida!")
else:
    print("Placa inválida.")
