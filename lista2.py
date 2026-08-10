


#encontra a posição do produto na lista
i = produtos.index('celular')
print(i)

#instancia a qtde de estoque para chegar a qtde de estoque do produto
qtde_estoque = estoque[1]
print('a quantidade de estoque de celular é: {}' .format(qtde_estoque))

#substitui o valor de uma lista / atenção para a variável instanciada!!!!
estoque[1] = 200
print('a quantidade de estoque de {} é: {}' .format(produtos[5], estoque[1]))