'''9. Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus
Celsius.C = (5 * (F-32) / 9).'''

f = float(input("Digite a temperatura em graus Farenheit: "))

c = (5 * (f - 32) / 9)

print("A temperatura em Celsius é %.2f" % c)


