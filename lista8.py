produtos = ['apple tv','mac','apple watch','mac book','airpod']
print(produtos)

tamanho_lista = len(produtos)
print('A lista tem {} produtos'.format(tamanho_lista))

produtos.append('iphone 17')
print(produtos)

# insere um valor na lista
produtos.append('table')
print(produtos)


tamanho_lista = len(produtos)
print('A lista tem {} produtos'.format(tamanho_lista))

# insere mais de um valor na lista
produtos.extend(['ipad','apple glass'])
print(produtos)

tamanho_lista = len(produtos)
print('A lista tem {} produtos'.format(tamanho_lista))
tamanho_lista = len(produtos)

vendas = [25,12,45,18,10,5,14,8]
maior_vendas = max(vendas) # traz o maior valor da lista
menor_vendas = min(vendas) # traz o menor valor da lista

# exibe os valores solicitado 
print('A maior venda {} vendas e a menor venda {}'.format(maior_vendas,menor_vendas))

# forma diferente mas mesmo resultado
print(f'A maior venda {maior_vendas} vendas e a menor venda {menor_vendas}')


i = vendas.index(maior_vendas)# index traz a posiçao da maior venda 
produto_mais_vendido = produtos[i]# o produto mais vendido esta na posiçao 3 e ele traz o valor do produto

print(f'o produto mais vendido e o {produto_mais_vendido}')

i = vendas.index(menor_vendas)
produtos_menos_vendido = produtos[i]

print(f'O produto menos vendido e o {produtos_menos_vendido} e a quantidade e {menor_vendas}')