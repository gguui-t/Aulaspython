cnpj = input("Digite o CNPJ: ")

cnpj_limpo = cnpj.replace(".", "").replace("/", "").replace("-", "")

if len(cnpj_limpo) == 14 and cnpj_limpo.isdigit():
    print(f"CNPJ limpo: {cnpj_limpo}")
else:
    print("Erro: o CNPJ deve conter exatamente 14 números.")
