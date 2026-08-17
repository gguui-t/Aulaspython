# Combinando for com if 

vendas = [1200,1500,300,800,900,100,450,3000,700,5000]

meta = 1200

# Quais valore bateram a meta 

for venda in vendas:
    if venda >= meta:
       print(vendas)

# Quantos valores bateram a meta 

metas_batidas = 0

for venda in vendas:
    if venda >= meta:
       metas_batidas +=1
print(metas_batidas)


qtde_funcionario = len(vendas)
print('o percentual de funcionarios que betram meta foi de {:.0%}' . format(metas_batidas/qtde_funcionario))


