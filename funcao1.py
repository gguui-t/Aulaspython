vendas = [1200,1500,300,800,900,100,450]
dias = ['segunda','terca','quarta','quinta','sexta','sabado','domingo']

# ordernar uma lista 

vendas.sort()
print(vendas)

# colocando listas em ordem crescente
vendas_crescente = sorted(vendas)
print(vendas_crescente)

# colocando listas em ordem decrescente
vendas_decrescente = sorted(vendas, reverse=True)
print(vendas_decrescente)

# contar os dias de vendas

dias_vendas = len(dias) # Len faz a contagem das posiçoes da lista
print('os dias de vendas foram {}' .format(dias_vendas))

#somar os valores de uma lista

total_vendas = sum(vendas)
print('o total das vendas foi {}' .format(total_vendas))

maior_venda = max(vendas)
menor_venda = min(vendas)
print('A maior venda foi {}' .format(maior_venda))
print('A menor venda foi {}' .format(menor_venda))

for i, venda in enumerate(vendas):
    print(f'venda no. {i} : {venda}')


# a funçao zip junta o valores das listas
for dia, venda in zip(dias,vendas):
    print(f' {dia} : {venda}')