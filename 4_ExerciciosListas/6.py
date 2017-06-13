'''
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
'''
medias = []
for i in range(1, 11):
    soma, media = 0, 0
    for y in range(1, 5):
        nota = float(input('Digite a %dº nota do %dº aluno: ' %(y, i)))
        soma += nota
    media = soma / 4
    medias.append(media)

print('Médias')
print(medias)

alunos = 0
for m in medias:
    if m >= 7:
        alunos +=1
print('Número de alunos com média maior ou igual a 7: %d' % alunos)
