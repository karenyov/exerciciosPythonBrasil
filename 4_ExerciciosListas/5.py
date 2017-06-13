'''
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''

par = []
impar = []
numeros = []
for i in range(1, 21):
    n = int(input('Digite o %dº número: ' %i))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    
    
print(numeros)
print('Par')
print(par)
print('Ímpar')
print(impar)
