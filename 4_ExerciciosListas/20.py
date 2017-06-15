'''
20 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores
em reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os
representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de
dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários
cujo salário for muito baixo, recebem este valor mínimo; Neste momento,
não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos,
impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário
de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero)
encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor
do abono concedido a cada colaborador, de acordo com a regra definida acima.
Ao final, o programa deverá apresentar:
'''

print('Digite 0 para encerrar o programa')
salarios = [] 
while True:
    salario = float(input('Salário: '))
    if salario == 0:
        break
    salarios.append(salario)

print('Projeção de Gastos com Abono')
print('============================')

print('Salário - Abono')
abonos, minimo = 0, 0
maior = 0
for s in salarios:
    abono = (salario * 20) / 100
    if abono < 100:
        abono = 100
        minimo += 1
    if abono > maior:
        maior = abono
    abonos += abono
    print('R$ %.2f - R$ %.2f' % (s, abono))

print('Foram processados %d colaboradores' % (sum(salarios)))
print('Total gasto com abonos: R$ %.2f' % abonos)
print('Valor mínimo pago a %d colaboradores' % minimo)
print('Maior valor de abono pago: R$ %.2f' % maior)
    
