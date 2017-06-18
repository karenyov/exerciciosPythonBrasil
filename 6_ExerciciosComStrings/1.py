'''
1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo
delas seguido do seu comprimento. Informe também se as duas strings possuem o
mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

print('Compara duas strings')
palavra1 = input('String 1: ')
palavra2 = input('String 2: ')

print('Tamanho de "%s": %d ' % (palavra1, len(palavra1)))
print('Tamanho de "%s": %d ' % (palavra2, len(palavra2)))

if len(palavra1) == len(palavra2):
    print('As duas strings são de tamanhos iguais')
else:
    print('As duas strings são de tamanhos diferentes')
    
if palavra1 == palavra2:
    print('As duas strings possuem conteúdo igual')
else:
    print('As duas strings possuem conteúdo diferente')
    



