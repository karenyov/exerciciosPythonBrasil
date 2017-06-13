'''
9 - Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numeros = []
for i in range(1, 11):
    n = int(input('Digite %dº número: ' % i))
    numeros.append(n)

for num in numeros:
    print('%d^2 = %d' % (num, (num**2)))
    


    
