'''
24. Faça um Programa que leia 2 números e em seguida pergunte ao
usuário qual operação ele deseja realizar. O
resultado da operação deve ser acompanhado de uma frase que diga
se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
'''

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operacao = int(input('Digite a operacao: 1-Adição, 2-Subtração, 3-Multiplicação, 4 Divisão: '))

if operacao == 1:
    resultado = numero1 + numero2
elif operacao == 2:
    resultado = numero1 - numero2
elif operacao == 3:
    resultado = numero1 * numero2
elif operacao == 4:
    resultado = numero1 / numero2

if resultado % 2 == 0:
    print('Número Par')
else:
    print('Número Ímpar')

if resultado < 0:
    print('Número negativo')
else:
    print('Número positivo')

if resultado == int(resultado):
    print('Número inteiro')
else:
    print('Número decimal')









