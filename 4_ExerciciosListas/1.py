'''
1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

numeros = []
for i in range(1, 6):
    n = int(input('Digite o %dº número: ' %i))
    numeros.append(n)

print(numeros)
