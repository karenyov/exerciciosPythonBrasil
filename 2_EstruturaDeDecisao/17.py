'''
17. Faça um Programa que peça um número correspondente a um
determinado ano e em seguida informe se este
ano é ou não bissexto.
'''

ano = int(input('Digite o valor do ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('%d é um ano bissexto' % ano)
else:
    print('%d não é um ano bissexto' % ano)







