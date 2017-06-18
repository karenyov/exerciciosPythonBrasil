'''
6. Data por extenso.
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''

data = input('Data de nascimento: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

dia = int(data[0:2])
mes = meses[int(data[3:5]) - 1]
ano = int(data[6:])

print('Você nasceu em %d de %s de %d' % (dia, mes, ano))



