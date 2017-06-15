'''
1. Faça um programa para imprimir:

 1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
'''
def lista(n):
    return list(str(n) * n)

n = int(input('Digite o número: '))

for i in range(1, n + 1):
    print(' '.join(lista(i)))

