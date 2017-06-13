'''
13 - Faça um programa que receba a temperatura média
de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

temperaturas = []
for i in range(1, 13):
    t = float(input('Digite a temperatura do %dº mês: ' % i))
    temperaturas.append(t)
media = sum(temperaturas) / 12

i = 0
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('Meses com temperatura acima da média')
for t in temperaturas:
    if t > media:
        print(meses[i])

    i += 1
        



    
