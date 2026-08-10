texto = 'debora.paixao@gmail.com'
nome ='Débora Regina Lopes da Paixão'

# 1a. letra maiúscula
print(texto.capitalize())

# 1a. letra maiúscula para cada palavra
print(texto.title())

# todas as letras minusculas
print(texto.casefold())

# todas as letras maiusculas
print(texto.upper())

# quantas vezes aparece o valor na string
print(texto.count('.'))

# verifica se o texto termina com um valor específico e a resposta é true ou false
print(texto.endswith('.com'))

# Procura um texto dentro de outro texto e dá como resposta a posição dentro da lista
print(texto.find('@'))

# lembrando  d e b o r a . p a i x  a  o  @  g  m  a  i  l  .  c  o  m
#            0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22

# Verifica se o texto é todo feito por caracteres alfanuméricos (letra e números)
print(nome.isalnum())

# Verifica se o texto é todo feito por caracteres alfabéticos
print(nome.isalpha())

# Verifica se o texto é todo feito por caracteres numérico


# Substitui um caracter por outro
moeda = '1000.00'
print(moeda.replace('.',','))

#separa um string de acordo com um delimitador
print(nome.split(' '))

#separa um texto de acordo com os "enters" que foram usados
frase = '''Olá! bom dia 
tudo bem?
a reunião é para falar sobre o faturamento.
faturamento = R$ 2.500,00
'''
print(frase.splitlines())