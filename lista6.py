#juntar e ordenar listas

produtos_loja1 = ['mouse','teclado','monitor','memoria']
print(produtos_loja1)
produtos_loja2 = ['tablet','notebook','filtro de linha','impressora']
print(produtos_loja2)

#unir duas listas
# lista1.extend(lista2)
# lista_atual = lista1 + lista2

produtos_loja1.extend(produtos_loja2)
produtos_lojas = produtos_loja1 + produtos_loja2
print(produtos_lojas)

