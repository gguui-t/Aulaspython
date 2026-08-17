produtos = ['tv','celular','table','notebook','mouse','teclado']
precos = [2500,1800,1500,3000,50,100]

#testando FOR EACH em uma lista de calculo de imposto

for preco in precos:
    print(f'{preco * 1.1:.2f}')

# testando for in range (percorrendo um lista com um indice)

for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto,preco)

# testando o Enumerate

for i, preco in enumerate(precos):
    produto = produtos[i]
    print(produto,preco)