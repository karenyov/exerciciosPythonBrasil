'''11. Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.'''

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = float(input("Digite o primeiro número real: "))

print("o produto do dobro do primeiro com metade do segundo é %d" % (numero1*2 + (numero2/2)))
print("a soma do triplo do primeiro com o terceiro.. é %d" % ((numero1*3) + numero3))
print("o terceiro elevado ao cubo é..%d" %(numero3 ** 3))




