# consultando valores dentro de uma lista

# execute os códigos para poder criar as variáveis
produtos = ['tv' , 'celular' , 'tablet', 'notebook', 'mouse', 'teclado']


#importante usar o método index, onde i é o nome padrão de um indice
# sintaxe: i = nome_da_lista.index('item)

#descobrir a qtde de estoque do produto mouse
i = produtos.index('mouse')
print(i) #ele traz a posição do produto na lista produtos
print(produtos[i]) # verificação do produto na posição

# verificar qtde de estoque do produto
qtde_estoque = estoque[i] # trazendo o mesmo indice do produto para o qtde de estoque
print(qtde_estoque)

print('Quantidade de estoque do mouse é {}' .format(qtde_estoque))

# usuario entra com o nome de um produto e o sistema retorna a posição dele

produto = input('Entre com o nome do produto em minuscula')
i = produtos.index(produto)
print(i)



# entrar com o nome do produto e o sistema traz a qtde de estoque dele

produto = input('Entre com o nome do produto em minuscula')
if produto in produtos:
    i = produtos.index(produto)
    print(i)
    qtde_estoque = estoque[i]
    print('A quantidade de {} no estoque é de {}' .format(produto, qtde_estoque))
else:
    print('Esse produto não existe no estoque')