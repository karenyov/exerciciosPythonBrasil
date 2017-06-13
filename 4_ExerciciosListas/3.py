'''
3- Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = []
for i in range(1, 5):
    n = float(input('Digite a %dº nota: ' % i))
    notas.append(n)
print(notas)
print('Média: %.2f' % (sum(notas)/4))
