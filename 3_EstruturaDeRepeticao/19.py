'''
19. Altere o programa anterior para que ele aceite
apenas números entre 0 e 1000.
'''

quantidade = int(input('Digite a quantidade de números: '))

i = 1
maior = 0
menor = 0
soma = 0
while i <= quantidade:
    while True:
        numero = int(input('Digite o %d número: ' % i))
        if numero > 0 and numero < 1000:
            break
        else:
            print('Número inválido. Digite novamente.')
    if i == 1:
        menor = numero
    if numero >= maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    i += 1
print('O maior número é %d' % maior)
print('O menor número é %d' % menor)
print('A soma dos números é %d' % soma)

    





    


    



