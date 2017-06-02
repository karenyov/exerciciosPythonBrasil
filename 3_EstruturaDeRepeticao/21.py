'''
21. Faça um programa que peça um número inteiro e determine se
ele é ou não um número primo. Um número
primo é aquele que é divisível somente por ele mesmo e por 1.
'''

numero = int(input('Digite um numero: '))

i = 1
cont = 0
while i <= numero:
    if numero % i == 0:
        cont += 1
    i += 1

if cont == 2:
    print('%d é primo' % numero)
else:
    print('%d não é primo' % numero) 




    





    


    



