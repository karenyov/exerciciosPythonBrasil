'''
13.Desenha moldura. Construa uma função que desenhe um retângulo usando
os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros,
linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a
1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles
devem ser modificados para valores dentro da faixa de forma elegante

'''

def valor_por_omissao(valor):
    if valor=='':
        return int(1)
    else:
        return faixa_minima_maxima(int(valor))

def faixa_minima_maxima(valor):
    if valor<1:
        return 1
    elif valor>20:
        return 20
    else:
        return valor

def cria_linha(linha):
    l='+'
    for x in range(linha):
        l+='-'
    l+='+'
    print (l)

def cria_coluna(linha, coluna):
    for y in range(coluna):
        c='|'
        c+= ' '*linha
        c+='|'
        print (c)

def desenha_moldura(linha, coluna):
    cria_linha(linha)
    cria_coluna(linha, coluna)
    cria_linha(linha)

linha=input('Diga quantos +----+, entre 1 e 20: ')
coluna=input('Diga quantos |    |, entre 1 e 20: ')
desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))
