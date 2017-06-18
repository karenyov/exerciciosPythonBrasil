'''
12. Valida e corrige número de telefone.
Faça um programa que leia um número de telefone, e corrija o número no
caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

'''

print('Valida e corrige número de telefone')
numero = int(input('Telefone: '))
novoNumero = ''
if len(str(numero)) < 8:
    diferenca = 8 - len(str(numero))
    novoNumero = '3' * diferenca

numeroFormatado = novoNumero + str(numero)
numeroFormatado = numeroFormatado[0:4] + '-' + numeroFormatado[5:]

print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))
print('Telefone corrigido sem formatação: %d' % numero)
print('Telefone corrigido com formatação: %s' % numeroFormatado)
