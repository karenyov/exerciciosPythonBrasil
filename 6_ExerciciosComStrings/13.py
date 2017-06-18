'''
13. Jogo da palavra embaralhada.
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que
será mostrada com as letras embaralhadas.
O programa terá uma lista de
palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela,
informando se o usuário ganhou ou perdeu o jogo.

'''

import random

print('Jogo da palavra embaralhada')

# Abre o arquivo para leitura
arquivo = open('palavras-exerc11.txt', 'r')

# Coloca todas as linhas em memoria
palavras = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

palavraEscolhida = palavras[random.randint(0, len(palavras) - 1)].upper().strip()
palavraEmbaralhada = ''.join(random.sample(palavraEscolhida,len(palavraEscolhida)))

print(palavraEmbaralhada)

for i in range(1, 7):
    p = input('Digite a palavra pela %dº: ' % i).upper()

    if p == palavraEscolhida:
        print('Você acertou!')
        break
    else:
        print('Você errou!')
    if i == 6:
        print('Você perdeu!')
        break
    
    
