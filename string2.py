faturamento = 2000
custo = 500
lucro = faturamento - custo

# usando o modelo str
print('O faturamento da loja foi de: ' + str(faturamento) + 'o lucro foi de: ' + str(lucro))

#usando o modelo .format()
print('o faturamento é de: {}' .format(faturamento))


#uma variação de .format()
print('O faturamento foi de: {} . O custo foi de: {}. O Lucro foi de: {}.' .format(faturamento, custo, lucro) )

#uma variação de .format() usando indices
print('O faturamento foi de: {0} . O custo foi de: {1}. O Lucro foi de: {2}. Lembrando que o custo foi: {1}' .format(faturamento, custo, lucro) )


#encapsulando texto
texto = 'O faturamento foi de: {}'
print(texto.format(faturamento))