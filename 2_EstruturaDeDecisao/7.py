'''
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
    if numero2 > numero3:
        menor = numero3
    else:
        menor = numero2
elif numero2 > numero3 and numero2 > numero1: 
    maior = numero2
    if numero3 > numero1:
        menor = numero1
    else:
        menor = numero3
else:
    maior = numero3
    if numero2 > numero1:
        menor = numero1
    else:
        menor = numero2

print('O maior é..%.2f' %maior)
print('O menor é..%.2f' %menor)
