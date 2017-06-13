'''
7 - Faça um Programa que leia um vetor de 5 números inteiros
, mostre a soma,
a multiplicação e os números.
'''
numeros = []
for i in range(1, 6):
    n = int(input('Digite o %dº número: ' %i))
    numeros.append(n)

soma = 0
multiplicacao = 1
for n in numeros:
    soma += n
    multiplicacao *= n

print('Soma dos números: %d' %soma)
print('Multiplicação dos números: %d' %multiplicacao)
    

