telefone = input('digite o numero do seu telefone: ')

if len(telefone) == 11 and telefone.isdigit():
    print("Telefone válido!")
else:
    print("Erro: o telefone deve conter exatamente 11 dígitos numéricos.")