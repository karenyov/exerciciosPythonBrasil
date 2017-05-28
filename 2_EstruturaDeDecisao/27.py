'''
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg Acima de 5 Kg
Morango R$ 2,50 por Kg R$ 2,20 por Kg
Maçã R$ 1,80 por Kg R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas
ou o valor total da compra ultrapassar R$ 25,00, receberá
ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de
morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.
'''

morangos = float(input('Digite a quantidade (em Kg) de morangos: '))
macas = float(input('Digite a quantidade (em Kg) de maças: '))

if morangos <= 5:
    preco1 = 2.5 * morangos
else:
    preco1 = 2.2 * morangos

if macas <= 5:
    preco2 = 1.8 * macas
else:
    preco2 = 1.5 * macas

valor = preco1 + preco2

if (morangos + macas) > 8 or valor > 25:
    desconto = (valor * 20) / 100
    valor = valor - desconto

print('Total: %.2f' % valor)








