'''
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
se a mesma é uma data válida.
'''

data = input('Digite a data: ')
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

if dia > 0 and dia <= 31:
    if mes > 0 and mes <= 12:
        if ano <= 0:
            print('Data inválida')
        else:
            print('Data válida')
    else:
        print('Data inválida')
else:
    print('Data inválida')









