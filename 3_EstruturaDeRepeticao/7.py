'''
7. Faça um programa que leia 5 números e informe o maior número.
'''

maior = 0
for i in range(1,6):
    numero = float(input('Digite o %dº número: ' %i))

    if numero > maior:
        maior = numero

print('O maior número é %.2f' % maior)


    


    



