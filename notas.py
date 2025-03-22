# sistema de notas de escola / média

print('sistema de notas de escola')

nome1 = input('Digite o nome do aluno')

nota1 = float(input('nota1'))
nota2 = float(input('nota2'))
nota3 = float(input('nota3'))
nota4 = float(input('nota4'))
nota5 = float(input('nota5'))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print('Aluno:')
print(nome1)
print(media)

aprovado = media >=7
reprovado = media <5
recuperacao = media >5 and media <7


#concatenar - juntar
print('Nome do aluno: ', nome1)
print('Media: ', media)
print('Notas: ', nota1, nota2, nota3, nota4, nota5)

print('Aprovado -', aprovado)
print('Reprovado -', reprovado)
print('Recuperação -', recuperacao) 


