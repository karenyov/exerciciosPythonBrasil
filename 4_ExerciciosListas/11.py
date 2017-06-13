'''
11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
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

print('Terceiro vetor')
vetor3 = []
for i in range(1, 11):
    n = int(input('Digite %dº número: ' % i))
    vetor3.append(n)

vetor4 = []
for i in range(0, 10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print(vetor3)
    


    
