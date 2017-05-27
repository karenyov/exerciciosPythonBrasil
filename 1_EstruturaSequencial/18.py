'''18. Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em
minutos).'''

tamanho = int(input('Digite o tamanho para download(em MB): '))
velocidade = float(input('Digite a velocidade(em Mbps): '))

bit = tamanho * 1024 * 2 * 8 
minutos = (bit / (velocidade * 1024 * 2)) / 60

print('Tempo aproximado para download(em min): %d' % minutos)
