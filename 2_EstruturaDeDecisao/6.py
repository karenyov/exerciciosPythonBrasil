'''
6. Faça um Programa que leia três números e mostre o maior deles.
'''

numero1 = float(input('Entre com o primeiro número: '))
numero2 = float(input('Entre com o segundo número: '))
numero3 = float(input('Entre com o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print('O maior é %.2f' % numero1)
elif numero2 > numero3:
    print('O maior é %.2f' %numero2)
else:
    print('O maior é %.2f' %numero3)




