'''
Faça um Programa que leia um vetor de 10
números reais e mostre-os na ordem inversa.
'''

numeros = []
for i in range(1, 11):
    n = int(input('Digite o %dº número: ' %i))
    numeros.append(n)
print(numeros[::-1])
