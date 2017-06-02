'''
22. Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo, por quais
número ele é divisível.
'''

numero = int(input('Digite um numero: '))

i = 1
cont = 0
while i <= numero:
    if numero % i == 0:
        cont += 1
    i += 1
print(cont)
if cont <= 2:
    print('%d é primo' % numero)
else:
    print('%d não é primo' % numero)
    print('Números divisíveis')
    y = 1
    while y <= numero:
        if numero % y == 0:
            print(y)
        y += 1





    





    


    



