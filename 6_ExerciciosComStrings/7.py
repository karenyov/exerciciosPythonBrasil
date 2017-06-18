'''
7. Conta espaços e vogais.
Dado uma string com uma frase informada pelo usuário
(incluindo espaços em branco), conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.
'''

frase = input('Digite a frase: ')
branco = 0
vogais = 0
for f in frase:
    if f == '':
        branco += 1
    if f in 'aeiou':
        vogais += 1

print('Total de espaços em branco: %d' % branco)
print('Total de vogais: %d' % vogais)





