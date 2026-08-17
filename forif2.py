funcionarios = [
    "Ana Silva",
    "Bruno Santos",
    "Carlos Oliveira",
    "Daniel Souza",
    "Eduardo Pereira",
    "Fernanda Costa",
    "Gabriel Almeida",
    "Helena Rodrigues",
    "Igor Martins",
    "Juliana Ferreira",
    "Lucas Gomes",
    "Mariana Carvalho",
    "Nathan Ribeiro",
    "Patrícia Barbosa",
    "Rafael Lima",
    "Sandra Araújo",
    "Thiago Nascimento",
    "Vanessa Teixeira",
    "William Cardoso",
    "Aline Mendes",
    "Beatriz Rocha",
    "Caio Moreira",
    "Débora Castro",
    "Felipe Dias",
    "Gustavo Freitas",
    "Isabela Moura",
    "João Correia",
    "Larissa Vieira",
    "Marcelo Ramos",
    "Natália Duarte"
]

for funcionario in funcionarios:
    print(funcionario)

for i, funcionario in enumerate(funcionarios):
    print('O nome do funcionario {} é {}' . format(i,funcionario))

# usando exemplo de produtos em estoque

produtos = ['coca cola', 'sprit', 'fanta' , 'guarana' , 'peps', 'dolly', 'Schweppes']
estoque = [550,300,500,450,800,650,200]
estoque_minimo = 500

for i,qtde in enumerate(estoque):
    if qtde < estoque_minimo:
        print('O produto {} esta abaixo do estoque minimo. Temos apenas {} unidades' .format(produtos[i], qtde))