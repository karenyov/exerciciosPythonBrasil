'''
49 -Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

Imprima no final a soma da série.

'''

numero = int(input('Informe a quantidade de termos: '))

seq, soma = 1, 0
for i in range(1, numero + 1):
    soma += i / seq
    seq += 2

print('Total da sequência: %.2f ' % soma)

