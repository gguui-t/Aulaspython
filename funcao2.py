import statistics

vendas = [150,90,2000,30,120,3,3,4,4,2,2,2]

media_vendas=(sum(vendas)/len(vendas))
print(media_vendas)

# media da lista
media = statistics.mean(vendas)
print(media)

# mediana para descobrir o valor central das vendas, especialmente quando existem valores muito altos ou muito baixos que podem distorcer a média.
mediana = statistics.median(vendas)
print(mediana)

# modal descobre o valor que mais se repete na lista
modal = statistics.mode(vendas)
print(modal)