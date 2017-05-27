'''8. Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''

valor = float(input("Digite o valor ganhado por hora: "))
horas = float(input("Digite o total de horas trabalhados no mês: "))

salario = valor * horas

print("Salário total é R$ %.2f" %salario)
