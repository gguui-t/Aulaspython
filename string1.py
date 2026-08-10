nome = 'debora'
email = 'debora.paixao@gmail.com'
print(nome)

#quando falamos de uma variável string o python sempre vai enxergar uma lista
#[D E B O R A]
#[0 1 2 3 4 5] *primerio item sempre começa na 0*

#para saber o tamanho de um texto em caracteres
print(len(nome))

#para "pegar um caracter especifico, precisa pegar o indice"
print(nome[4])

#para pegar o ultimo ou os penultimos itens de uma lista de texto
print (email[-1])

#para pegar à partir de um caracter
print(email[6:]) #à partir do 6 , com o 6 inclusive

#para pegar até um caracter específico
print(email[-10:]) 

#para pegar até um caracter específico no meio do valor
print(email[5:8]) 

#quando os dois pontos estão no início, ele não inclui o indice
print(email[:10]) 

#quando precisa de um trecho do texto usar o ':'

print('tamanho do email' + str(len(email)) + 'caracteres')
print('primeiro caracter do email: ' + email[0])
print('ultimo caracter do email: ' + email[-1])
print('servidor do email: ' + email[13:])