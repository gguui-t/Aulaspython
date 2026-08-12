nome_completo = input("Digite o nome completo: ")

partes = nome_completo.split()

primeiro_nome = partes[0]
sobrenome = partes[-1]

username = primeiro_nome[0] + sobrenome

print(f"Username: {username.lower()}")
