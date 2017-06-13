'''
8 - Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idades = []
alturas = []
for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)

print('Ordem inversa')
print('Alturas')
print(alturas[::-1])
print('Idades')
print(idades[::-1])

print('Ordem lida')
print('Alturas')
print(alturas)

print('Idades')
print(idades)

    
