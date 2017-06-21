'''
1. Faça um programa que leia um arquivo texto contendo uma lista de endereços
IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e
inválidos.
O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''

import random

def validaIP(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            return False
    return True

# Abre o arquivo para leitura
arquivo = open('entrada-exerc01.txt', 'r')

# Coloca todas as linhas em memoria
linhas = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

validos = []
invalidos = []
for l in linhas:
    validaIP(l)
    if validaIP(l):
        validos.append(l)
    else:
        invalidos.append(l)

# Abre o arquivo para escrita
arquivo = open('saida-exerc01.txt', 'w')

arquivo.write('[Endereços válidos:]\n')
for v in validos:
    arquivo.write(v)
arquivo.write('[Endereços inválidos:]\n')
for i in invalidos:
    arquivo.write(i)

# Fecha o arquivo
arquivo.close()



    



