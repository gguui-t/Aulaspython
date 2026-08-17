# criando a propria função 

def cadastrar_produtos():
    produto = input('Digite o nome do produto a ser cadastrado: ')
    produto = produto.casefold() # funcao casefold diminiu as letras
    print(' produto {} cadastrado com sucesso!!' .format(produto))

cadastrar_produtos()