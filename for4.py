
vendas = [
    ['joao',1500],
    ['pedro',800],
    ['larissa',2000],
    ['paulo',300],
    ['gabriel',1000],
    ['bruna',500]
]

meta_venda = 1000

for item in vendas:
    if item[1] >= meta_venda:
        print('vendedor {} bateu a meta!! fez {} em vendas' .format(item[0],item[1]))