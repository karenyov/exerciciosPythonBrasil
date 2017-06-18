'''
11. Jogo de Forca.
Desenvolva um jogo da forca.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''
import random

print('Jogo de Forca')

# Abre o arquivo para leitura
arquivo = open('palavras-exerc11.txt', 'r')

# Coloca todas as linhas em memoria
palavras = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

palavraEscolhida = palavras[random.randint(0, len(palavras) - 1)].upper().strip()
tamanhoPalavra = len(palavraEscolhida)
palavraAdivinhada = ['_'] * tamanhoPalavra

numTentativas = 0
erros = 0

print(' '.join(palavraAdivinhada))
print(palavraEscolhida)
while True:
    p = input('Digite a letra: ')
    cont = 0
    if p in palavraEscolhida: #letra encontrada
        for pa in palavraEscolhida:
            if pa == p: #letra encontrada e posição
                palavraAdivinhada[cont] = p
            cont += 1
        if '_' not in ' '.join(palavraAdivinhada):
            print('Você ganhou!')
            break
    else:
        erros += 1
        if erros >= 6:
            print('Você perdeu a palavra é %s' % palavraEscolhida)
        else:
            print('Você errou pela %dº vez. Tente novamente.' % erros)
    print(' '.join(palavraAdivinhada))
    


