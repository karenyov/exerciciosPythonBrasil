'''
34. Os números primos possuem várias aplicações dentro
da Computação, por exemplo na Criptografia. Um
número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um
número inteiro e determine se ele é ou não um número primo.
'''

numero = int(input('Digite o número: '))
cont = 0
for i in range(1, numero + 1):
    
    if numero % i == 0:
        cont += 1
if cont <= 2:
    print('É um número primo')
else:
    print('Não é um número primo')
    

            



        




    





    


    



