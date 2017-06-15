'''
24 - Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.

'''
import random

numeros = [0] * 6
for i in range(1, 100):
    n =  random.randint(1, 6)
    numeros[n -1] = numeros[n -1] + 1

cont = 1 
for n in numeros:
    print('%d teve %d lançamentos' % (cont, n))
    cont += 1
    
