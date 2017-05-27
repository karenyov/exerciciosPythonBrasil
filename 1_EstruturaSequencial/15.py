'''15. Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que
são descontados 11% para o Imposto
de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor = float(input("Digite o valor por hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês: "))

v = valor * horas

ir = ((valor * 11) / 100)
inss = ((valor * 8) / 100)
s = ((valor * 5) / 100)

descontos = ir + inss + s

print('Salário bruto R$ %.2f' % v)
print('INSS %.2f' % inss)
print('Sindicato %.2f' %s)
print('Salário Líquido R$ %.2f' % (v - descontos))





