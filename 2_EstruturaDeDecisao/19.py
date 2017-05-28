'''
19. Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas
e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
11, 1, 7 e 16
'''

numero = int(input('Digite um número: '))
numeroStr = str(numero)
qtNumero = len(numeroStr)

if qtNumero == 3:
    centena = numeroStr[0:1]
    dezena = numeroStr[1:2]
    unidade = numeroStr[2:3]
    print (numeroStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")

if qtNumero == 2:
    dezena = numeroStr[0:1]
    unidade = numeroStr[1:2]
    print (numeroStr+" = "+dezena+" dezenas, "+unidade+ " unidades")

if qtNumero == 1:
    unidade = numeroStr[0:1]
    print (numeroStr+" = "+unidade+ " unidades")










