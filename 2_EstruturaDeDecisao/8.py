'''
8. Faça um programa que pergunte o preço de três produtos e
informe qual produto você deve comprar, sabendo
que a decisão é sempre pelo mais barato.
'''

produto1 = float(input('Digite o preço do produto 1: '))
produto2 = float(input('Digite o preço do produto 2: '))
produto3 = float(input('Digite o preço do produto 3: '))

if produto1 < produto2 and produto1 < produto3:
    barato = produto1
elif produto2 < produto1 and produto2 < produto3:
    barato = produto2
else:
    barato = produto3

print('O produto mais barato é..%.2f' % barato)

