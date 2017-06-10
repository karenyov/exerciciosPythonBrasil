'''
47 - Em uma competição de ginástica, cada atleta recebe votos
de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e
as notas dos sete jurados alcançadas pelo atleta em sua apresentação
e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as
notas restantes). As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''
notas = []
melhor, pior = 0, 0 
nome = input('Digite o nome do atleta: ')
for i in range(1, 8):
    notas.append(float(input('Digite a nota do %dº jurado: ' % i)))
notas.sort()
melhor = notas[-1]
pior = notas[0]
notas = notas[1:-1]
    
media = sum(notas) / 5
print('Resultado final: ')
print('Atleta: %s' % nome)
print('Melhor nota %.2f' % melhor)
print('Pior nota: %.2f' % pior)
print('Média: %.2f' % media)
    
    

