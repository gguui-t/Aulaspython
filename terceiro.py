nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = (nota1+nota2)/2

print("A media das notas é: " , media)

if media >= 7:
    print("Aluno Aprovado")
elif media>=5:
    print("Aluno de recuperação")
else:
    print("aluno reprovado")