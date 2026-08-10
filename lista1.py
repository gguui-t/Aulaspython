
# nem sempre será assim ,mas as listas foram feitas para serem homogeneas (só textos ou só com números)
# muito importante para a importação de dados externos
produtos = ['tv' , 'celular' , 'tablet', 'notebook', 'mouse', 'teclado']
precos = [2500, 1800, 1500, 3000, 50 , 100]
print(produtos) #exibição da lista toda
print(precos)  #exibição da lista toda

print(produtos[3]) #exibição de um item daa lista
print(precos[5])  #exibição de um item daa lista

print('O produto {} tem o preco {}'.format(produtos[1], precos[1]))