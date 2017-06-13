'''
10 - Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores.
'''

print('Primeiro vetor')
vetor1 = []
for i in range(1, 11):
    n = int(input('Digite %dº número: ' % i))
    vetor1.append(n)

print('Segundo vetor')
vetor2 = []
for i in range(1, 11):
    n = int(input('Digite %dº número: ' % i))
    vetor2.append(n)

vetor3 = []
for i in range(0, 10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor3)


    


    
