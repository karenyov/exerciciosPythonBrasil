'''
35. Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário.
'''

numero = int(input('Digite o número: '))

for i in range(1, numero + 1):
    cont = 0
    for y in range(1, i + 1):
        if i % y == 0:
            cont += 1
    if cont == 2:
        print('%d é um número primo.' %i)
    else:
        print('%d não é um número primo.' %i)
    
    
            



        




    





    


    



