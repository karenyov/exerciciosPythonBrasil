'''
21. Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e
depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e
100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a
quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa
fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa
fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

saque = int(input('Digite o valor do saque: '))

nota = (saque // 100)
saque = (saque - (nota * 100))
print('%.2f notas de 100' % nota)

nota = (saque // 50)
saque = (saque - (nota * 50))
print('%.2f notas de 50' % nota)

nota = (saque // 10)
saque = (saque - (nota * 10))
print('%.2f notas de 10' % nota)

nota = (saque // 5)
saque = (saque - (nota * 5))
print('%.2f notas de 5' % nota)

nota = (saque // 1)
saque = (saque - (nota * 1))
print('%.2f notas de 1' % nota)








