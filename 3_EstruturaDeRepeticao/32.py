'''
32. Faça um programa que calcule o fatorial de um número
inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A
saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! = 5 . 4 . 3 . 2 . 1 = 120
'''

numero = int(input('Digite o número: '))
total = 1
print('Fatorial de: %d' % numero)
print('%d! = ' % numero, end=' ')
for i in range(numero, 1, -1):
    total *= i
    print('%d' %i, end = '.')
print('1 = %d' %total)


            



        




    





    


    



