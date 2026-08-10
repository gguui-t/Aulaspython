# inserindo e removendo um item da lista

produtos = ['apple tv','mac','iphone x','ipad','apple watch','mac book','airpods']
print(produtos)

# para adicionar um item
# nome_da_lista.append('nome_do_item')
produtos.append('iphone 11')
print(produtos)

#somente substituir um valor por outro
produtos[1]='tac'
print(produtos)

# remover um item da lista usando REMOVE
produtos.remove('iphone x')
print(produtos)

# tratando um erro

produto_apagado = input('digite o nome do produto a seer apagado')
if produto_apagado in produtos:
    produtos.remove(produto_apagado)
    print(produtos)
else:
    print('esse produto não se encontra nessa lista')

# remover um item da lista usando o POP
item_removido = produtos.pop(3)
print(produtos)
print('o item removido foi o {}' .format(item_removido))
