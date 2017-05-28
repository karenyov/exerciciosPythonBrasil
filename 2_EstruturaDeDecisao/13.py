'''
13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda,
etc.), se digitar outro valor deve aparecer valor inválido.
'''

numero = int(input('Digite o dia da semana(1-Domingo, 2-Segunda, etc): '))

if numero == 1:
    semana = 'Domingo'
elif numero == 2:
    semana = 'Segunda-feira'
elif numero == 3:
    semana = 'Terça-feira'
elif numero == 4:
    semana = 'Quarta-feira'
elif numero == 5:
    semana == 'Quinta-feira'
elif numero == 6:
    semana == 'Sexta-feira'
elif numero == 7:
    semana = 'Sábado'
else:
    semana = 'Valor inválido'

print(semana)

