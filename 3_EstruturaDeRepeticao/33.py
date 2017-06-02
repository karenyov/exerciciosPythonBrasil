'''
33. O Departamento Estadual de Meteorologia lhe contratou para
desenvolver um programa que leia as um
conjunto indeterminado de temperaturas, e informe ao final a
menor e a maior temperaturas informadas, bem
como a média das temperaturas.
'''

maior = 0
menor = 0
i = 1
print('Digite -1 para sair')
while True:
    temperatura = float(input('Digite a temperatura: '))
    if temperatura == -1:
        break
    if i == 1:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
        
    if temperatura <= menor:
        menor = temperatura
    i += 1
        
print('Maior temperatura: %.2f' % maior)
print('Menor temperatura: %.2f' % menor)

    

            



        




    





    


    



