'''
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro
d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f. acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o
tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
o preço do litro do álcool é R$
1,90.
'''

litros = float(input('Digite a quantidade em litros: '))
combustivel = input('Digite o tipo de combustível A-álcool, G-gasolina: ').upper()

if combustivel == 'A':
    preco = litros * 1.9
    if litros <= 20:
        desconto = litros * ((preco * 3) / 100)
    else:
        desconto = litros * ((preco * 5) / 100)
    print('R$ %.2f' % (preco - desconto))

elif combustivel == 'G':
    preco = litros * 2.5
    if litros <= 20:
        desconto = litros * ((preco * 4) / 100)
    else:
        desconto = litros * ((preco * 6) / 100)
    print('R$ %.2f' %(preco - desconto))
else:
    print('Tipo inválido')
    











