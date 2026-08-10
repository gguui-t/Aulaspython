produtos = ['apple tv','mac','apple watch','mac book','airpod']
print(produtos)
# para inserir um novo valor em uma nova posiçao dentro da lista
produtos.append('iphone 17')
print(produtos)

# substituir um valor por outro na mesma posiçao da lista
produtos[1] = 'tac'
print(produtos)

# remove um item da lista 
#produtos.remove = ('iphone')
print(produtos)

# remover um valor externo

produto_apagado = input('Digite o nome do produto a ser removido: ')
if produto_apagado in produtos:
   produtos.remove = (produto_apagado)
   print(produtos)
else: 
   print('Produto inexistente na lista!!')

# outra forma e remover!!
# produtos.remove(input("Digite o valor a ser removido: "))