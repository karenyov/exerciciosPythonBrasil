'''
12 - Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13
anos possuem altura inferior à média de altura desses alunos.
'''

idades = []
alturas = []
for i in range(1, 31):
    idade = int(input('Digite a idade do %dº aluno: ' % i))
    altura = float(input('Digite a altura do %dº aluno: ' % i))
    idades.append(idade)
    alturas.append(altura)

media = sum(alturas) / 30
total = 0
for i in range(0, 30):

    if idades[i] > 13 and alturas[i] < media:
        total += 1

print('Total de alunos com mais de 13 anos e altura inferio a media de altura: %d' % total)
        
    
    

    


    
