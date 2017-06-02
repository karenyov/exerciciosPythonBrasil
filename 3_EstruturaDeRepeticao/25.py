'''
25. Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de
idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada.
'''

p = int(input('Entre com a quantidade de pessoas: '))
soma = 0
for i in range(1, p + 1):
    idade = int(input('Digite a idade da %d pessoa: ' % i))
    soma += idade

media = soma / p
if media >= 0 and media <= 25:
    print('Turma é jovem')
elif media >= 26 and media <= 60:
    print('Turma é adulta')
elif media > 60:
    print('Turma idosa')
    
    
        
            
        




    





    


    



