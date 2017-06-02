'''
28. Faça um programa que calcule o valor total investido
por um colecionador em sua coleção de CDs e o valor
médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs
e o valor para em cada um.
'''

cds = int(input('Digite a quantidade de CDs: '))
total = 0
for i in range(1, cds + 1):
    valor = float(input('Digite o valor do %dº cd: ' %i))
    total += valor
print('Valor total gasto %.2f' %total)
print('Média do valor gasto %.2f' % (total/cds))

        




    





    


    



