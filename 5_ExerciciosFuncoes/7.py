'''
7. Faça um programa que use a função valorPagamento para determinar
o valor a ser pago por uma prestação de uma conta.
O programa deverá
solicitar ao usuário o valor da prestação e o número de dias em atraso
e passar estes valores para a função valorPagamento, que calculará o
valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor
de prestação e assim continuar até que seja informado um valor
igual a zero para a prestação. Neste momento o programa deverá
ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia. O cálculo do valor a
ser pago é feito da seguinte forma.
Para pagamentos sem atraso,
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de
multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(valor, dias):
    juros = 0
    if dias == 0:
        return valor
    else:
    else:
        juros = (0.1/100 * dias) * valor
        
        return valor + (valor * (3/100)) + juros 

total = 0
cont = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break
    dias = int(input('Digite o número de dias em atraso: '))
    total += valorPagamento(valor, dias)
    cont += 1

print('Quantidade total: %d' % cont)
print('Valor total das prestações: %.2f' % total)



