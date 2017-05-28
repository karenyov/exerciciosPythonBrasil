'''
14. Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um
semestre, e calcule a sua média. A atribuição de conceitos obedece
à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito
correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
aproveitamento = ''
mensagem = ''

if media > 9 and media <= 10:
    aproveitamento = 'A'
elif media > 7.5 and media <= 9:
    aproveitamento = 'B'
elif media > 6.0 and media <= 7.5:
    aproveitamento = 'C'
elif media > 4.0 and media <= 6.0:
    aproveitamento = 'D'
elif media >= 4.0 and media >= 0:
    aproveitamento = 'E'

if aproveitamento in 'ABC':
    mensagem = 'APROVADO'
elif aproveitamento in 'DE':
    mensagem = 'REPROVADO'

print('Nota 1: %.2f' % nota1)
print('Nota 2: %.2f' % nota2)
print('Média: %.2f' % media)
print('Aproveitamento: %s' % aproveitamento)
print(mensagem)




