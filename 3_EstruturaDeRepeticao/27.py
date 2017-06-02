'''
27. Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e
a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
'''

turmas = int(input('Digite a quantidade de turmas: '))
soma = 0
for i in range(1, turmas + 1):
    while True:
        alunos = int(input('Digite a quantidade de alunos para a %dº turma: ' %i))
        if alunos <= 40:
            break
        else:
            print('As turmas não podem ter mais de 40 alunos. Digite novamente.')
    soma += alunos

print('O número médio de alunos por turma é %.2f' % (soma / turmas))

    
        
            
        




    





    


    



