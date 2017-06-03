'''
41. Faça um programa que receba o valor de uma dívida e mostre
uma tabela com os seguintes dados: valor da
dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
R$ 1.000,00 0 1 R$ 1.000,00
R$ 1.100,00 100 3 R$ 366,00
R$ 1.150,00 150 6 R$ 191,67
'''

valor = float(input('Digite o valor da dívida: '))

print('Quantidade de Parcelas % de Juros sobre o valor inicial da dívida')

print('%d %d' %(1, 0))
juros = 0
for i in range(1, 5):
    print('%d %d' %((i * 3), juros))
    juros += 5

p = 1
juros = 0
for i in range(1, 6):
    valorJuros = (valor * juros) / 100
    valorDivida = valor + valorJuros
    valorParcela = valorDivida / p
    print('%.2f %.2f %d %.2f' %(valorDivida, valorJuros, p, valorParcela))
    
    if i == 1:
        juros = 10
        p = 3
    else:
        juros += 5
        p += 3
    

