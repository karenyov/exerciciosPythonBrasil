'''
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))


if numero1 > numero2 and numero1 > numero3:
    maior = numero1
    if numero2 > numero3:
        menor = numero3
        meio = numero2
    else:
        menor = numero2
        meio = numero3
elif numero2 > numero3 and numero2 > numero1: 
    maior = numero2
    if numero3 > numero1:
        menor = numero1
        meio = numero3
    else:
        menor = numero3
        meio = numero1
else:
    maior = numero3
    if numero2 > numero1:
        menor = numero1
        meio = numero2
    else:
        menor = numero2
        meio = numero1

print('Ordem decrescente %.2f , %.2f, %.2f' % (maior, meio, menor))
