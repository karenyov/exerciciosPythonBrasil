'''
39. Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o
segundo representando a sua altura em centímetros. Encontre o aluno mais
alto e o mais baixo. Mostre o
número do aluno mais alto e o número do aluno mais baixo, junto com suas
alturas.
'''

numeroAlto = 0
numeroBaixo = 0

alturaAlto = 0
alturaBaixo = 0

for i in range(1, 11):
    numero = int(input('Digite o número do %dº aluno: ' % i))
    altura = float(input('Digite a altura do %dº aluno: ' % i))

    if i == 1:
        numeroBaixo = numero
        alturaBaixo = altura

    if altura > alturaAlto:
        numeroAlto = numero
        alturaAlto = altura

    if altura < alturaBaixo:
        numeroBaixo = numero
        alturaBaixo = altura

print('Aluno mais Alto')
print('Número do aluno: %d' % numeroAlto)
print('Altura do aluno: %d' % alturaAlto)

print('Aluno mais Baixo')
print('Número do aluno: %d' % numeroBaixo)
print('Altura do aluno: %d' % alturaBaixo)      
        
        
        

    
    
    

