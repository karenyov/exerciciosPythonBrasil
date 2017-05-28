'''
12. Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00
'''

valor = float(input('Digite o valor da hora: '))
hora = int(input('Digite a quantidade de horas trabalhadas: '))

bruto = valor * hora

if bruto <= 900.00:
    descontoIR = 0
elif bruto > 900.00 and bruto <= 1500.00:
    descontoIR = 5
elif bruto > 1500.00 and bruto <= 2500:
    descontoIR = 10
elif bruto > 2500:
    descontoIR = 20

inss = (bruto * 10) /100.00
fgts = (bruto * 11) / 100.00
ir = (bruto * descontoIR)/ 100.00
sin = (bruto * 3) / 100

descontos = ir + inss

print('Salário Bruto: (%d * %.2f): %.2f' %(hora, valor, bruto))
print('(-) IR (%.2f%%): R$ %.2f' % (descontoIR, ir))
print('(-) INSS (10%%): %.2f' % inss)
print('FGTS (11%%): R$ %.2f' % fgts)
print('Total de Descontos: R$ %.2f' % descontos)
print('Salário Liquido %.2f' % (bruto - descontos))
