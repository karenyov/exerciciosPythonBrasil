'''
20. Altere o programa de cálculo do fatorial,
permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
'''

quantidade = int(input('Digite a quantidade: '))

for i in range(1, quantidade + 1):

    while True:
        numero = int(input('Digite o %dº número: ' % i))

        if numero < 16:
            break
        else:
            print('Número inválido. Digito novamente.')

    y = 1
    fatorial = 1
    while y <= numero:
        fatorial *= y
        y  += 1
        
    print(fatorial)



    





    


    



