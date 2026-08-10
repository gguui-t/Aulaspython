senha = input('digite sua senha: ')

senha_oculta = senha[:2] + '*' * (len(senha) - 4) + senha[-2:]

print(senha_oculta)