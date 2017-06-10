'''
45 - Desenvolver um programa para verificar a nota do aluno em uma prova com
10 questões, o programa deve perguntar ao aluno a resposta de cada questão
e ao final comparar com o gabarito da prova e assim calcular o total de
acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se
outro aluno vai utilizar o sistema. Após todos os alunos terem respondido
informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo
que o professor digite
o gabarito da prova antes dos alunos usarem o programa.
'''
maior = 0
menor = 0
total = 0
resp1 = input('Digite a resposta da 1º questão: ')
resp2 = input('Digite a resposta da 2º questão: ')
resp3 = input('Digite a resposta da 3º questão: ')
resp4 = input('Digite a resposta da 4º questão: ')
resp5 = input('Digite a resposta da 5º questão: ')
resp6 = input('Digite a resposta da 6º questão: ')
resp7 = input('Digite a resposta da 7º questão: ')
resp8 = input('Digite a resposta da 8º questão: ')
resp9 = input('Digite a resposta da 9º questão: ')
resp10 = input('Digite a resposta da 10º questão: ')
totalAcertos = 0
while True:
    acertos = 0
    erros = 0
    for i in range(1, 11):
        resposta = input('Digite a resposta da %d questão: ' % i).upper()
        if i == 1:
            if resp1 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 2:
            if resp2 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 3:
            if resp3 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 4:
            if resp4 == resposta:
                acertos += 1
            else:
                erros += 1  
        if i == 5:
            if resp5 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 6:
            if resp6 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 7:
            if resp7 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 8:
            if resp8 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 9:
            if resp9 == resposta:
                acertos += 1
            else:
                erros += 1
        if i == 10:
            if resp10 == resposta:
                acertos += 1
            else:
                erros += 1
    if acertos > maior:
        maior = acertos
    total += 1
    totalAcertos += acertos
    if total == 1:
        menor = acertos
    if acertos < menor:
        menor = acertos
    continuar = int(input('Digite 0 para sair 1 para continuar: '))
    if continuar == 0:
        break
print('Maior acerto %d' % maior)
print('Menor acerto %d' % menor)
print('Total de alunos: %d' %total)
print('Média das notas %.2f' % ( totalAcertos/ total))
