'''
20. Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média
alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a
respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a r
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Aprovado! Média: %.2f' % media)
else:
    print('Reprovado! Média: %.2f' % media)










