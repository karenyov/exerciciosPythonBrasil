'''
2. Faça um programa para imprimir:
 1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário.
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

'''

n = int(input('Digite o número: '))

def lista(n):
    for i in range(1, n + 1):
        l = []
        for j in range(i):
            l.append(str(j+1))
        print(' '.join(l))
lista(n)
