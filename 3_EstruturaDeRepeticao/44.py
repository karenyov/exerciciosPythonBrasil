'''
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.
'''

print('Votos')
print('Cod / Candidato')
print('1 / José')
print('2 / João')
print('3 / Maria')
print('4 / Raquel')
print('5 / Voto Nulo')
print('6 / Voto em Branco')
print('Digite 0 para finalizar')

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
nulo = 0
branco = 0
total = 0 
while True:
    voto = int(input('Digite o código do voto: '))
    if voto == 0:
        break
    if voto == 1:
        cont1 += 1
    if voto == 2:
        cont2 += 1
    if voto == 3:
        cont3 += 1
    if voto == 4:
        cont4 += 1
    if voto == 5:
        nulo += 1
    if voto == 6:
        branco += 1
    total += 1
        
print('Total de votos para José: %d' % cont1)
print('Total de votos para João: %d' % cont2)
print('Total de votos para Maria: %d' % cont3)
print('Total de votos para Raquel: %d' % cont4)

print('Total de votos Nulo: %d' % nulo)
print('Total de votos em Branco: %d ' % branco)
print('Percentual de votos nulos: %.2f%%' % (nulo / total * 100))
print('Percentual de votos em branco: %.2f%%' % (branco / total * 100))
    
    
