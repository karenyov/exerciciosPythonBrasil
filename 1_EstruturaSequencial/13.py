'''13. Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso
ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7 (h = altura)
c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.'''

altura = float(input("Entre com a altura: "))
sexo = input("Entre com o sexo F-Feminino ou M-Masculino: ")
p = float(input("Digite seu peso: "))

if sexo == 'F':
    peso = (62.1*altura) - 44.7
else:
    peso = (72.7*altura) - 58

print("Peso Ideal %.2f" % peso)

if p > peso:
    print('Você está acima do peso')
else:
    print('Você está abaixo do peso')





