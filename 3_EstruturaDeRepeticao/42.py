'''
42. Faça um programa que leia uma quantidade indeterminada de
números positivos e conte quantos deles estão
nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido
um número negativo.
'''

n = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
while n >= 0:
    n = int(input('Digite o número: '))
    if n >=0 and n <= 25:
        i1 += 1
    if n >= 26 and n <= 50:
        i2 += 1
    if n >= 51 and n <= 75:
        i3 += 1
    if n >= 76 and n <= 100:
        i4 += 1

    
print('[0-25] = %d' % i1)
print('[26-50] = %d' % i2)
print('[51-75] = %d' % i3)
print('[76-100] = %d' % i4)
