'''
37. Uma academia deseja fazer um senso entre seus clientes
para descobrir o mais alto, o mais baixo, a mais
gordo e o mais magro, para isto você deve fazer um programa
que pergunte a cada um dos clientes da
academia seu código, sua altura e seu peso. O final da digitação
de dados deve ser dada quando o usuário
digitar 0 (zero) no campo código. Ao encerrar o programa também
deve ser informados os códigos e valores do
clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos
clientes
'''

codAlto = 0
valorAlto = 0

codBaixo = 0
valorBaixo = 0

codGordo = 0
valorGordo = 0

codMagro = 0
valorMagro = 0

mediaAltura = 0
mediaPeso = 0

somaAltura = 0
somaPeso = 0

i = 1
while True:
    codigo = int(input('Digite seu código: '))
    if codigo == 0:
        break
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    if i == 1:
        codBaixo = codigo
        valorBaixo = altura
        codMagro = 0
        valorMagro = 0

    if peso > valorGordo:
        codGordo = codigo
        valorGordo = peso
    if peso < valorGordo:
        codMagro = codigo
        valorMagro = peso
        
    if altura > valorAlto:
        codAlto = codigo
        valorAlto = altura
    if altura < valorBaixo:
        codBaixo = codigo
        valorBaixo = altura
    i += 1

    somaAltura += altura
    somaPeso += peso

print('Cliente mais Baixo')
print('Cód: %d' % codBaixo)
print('Altura: %.2f' % valorBaixo)

print('Cliente mais Alto')
print('Cód: %d' % codAlto)
print('Altura: %.2f' % valorAlto)

print('Cliente com menos Peso')
print('Cód: %d' % codMagro)
print('Peso: %.2f' % valorMagro)

print('Cliente com mais Peso')
print('Cód: %d' % codGordo)
print('Peso: %.2f' % valorGordo)
        
    
    
            



        




    





    


    



