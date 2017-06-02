'''
14. Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a
quantidade de números impares.
'''
pares = 0
impares = 0
for i in range(1, 11):
    numero = int(input('Digita o número: '))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print('Quant. de números pares %d' %pares)
print('Quant. de números ímpares %d' %impares)
    




    


    



