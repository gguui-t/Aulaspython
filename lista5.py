
produtos = ['apple tv','mac','iphone x','ipad','apple watch','mac book','airpods']

# tamanho de uma lista, maior e menor valor
tamanho_lista = len(produtos)
print('nessa listas existem {} produtos' .format(tamanho_lista))


# encontrar o maior valor de uma lista
vendas = [25, 18, 15, 30, 5 , 10, 20]

maior_venda = max(vendas)
menor_venda = min(vendas)

print('a maior venda é {} e  menor venda é {}' .format(maior_venda,menor_venda))

#encontrando o produto mais vendido

i = vendas.index(maior_venda)
produto_mais_vendido = produtos[i]
print('o produto mais vendido é {}' .format(produto_mais_vendido))
