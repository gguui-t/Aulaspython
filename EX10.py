email = input("Digite o e-mail do funcionário: ").strip()

if email.endswith("@hashtag.com"):
    print("E-mail corporativo válido.")
else:
    print("Erro: o e-mail deve ser do domínio da empresa (@hashtag.com).")
