'''
Faça um Programa que leia um vetor de 10 caracteres, e diga
quantas consoantes foram lidas.
Imprima as consoantes.
'''

c = []
vogal = 'aeiou'
consoantes = 0
for i in range(1, 11):
    letra = input('Digite o %dº caractere: ' % i).lower()

    if letra not in vogal:
        consoantes += 1
        c.append(letra)

print('Total de consoantes: %d' % consoantes)
print(c)

    

