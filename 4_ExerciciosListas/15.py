'''
15 - Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for
informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados,
um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

notas = []
print('Digite -1 para encerrar o programa')
while True:
    nota = float(input('Digite a nota: '))
    if nota < 0:
        print('O programa foi encerrado')
        break
    notas.append(nota)

media = sum(notas) / len(notas)
acima = 0
abaixo = 0
for n in notas:
    if n > media:
        acima += 1
    if n < 7:
        abaixo += 1

print('Quantidade de valores lidos: %d' % (len(notas)))
print('A soma dos valores é: %.2f' % (sum(notas)))
print('Quantidade de valores acima da média %d' % acima)
print('Quantidade de valores abaixo de sete: %d' % abaixo)
    
    
    
    





    
