'''
51 - Faça um programa que mostre os n termos da Série a seguir:

Imprima no final a soma da série.
'''

n = int(input('Digite o número: '))
s = 0
d = 1
for i in range(1, n + 1):
    s += i / d
    d += 2
print('Soma da sequência: %.2f' % s)
    
