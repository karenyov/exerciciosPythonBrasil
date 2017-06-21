'''
2. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de
espaço em disco no seu servidor de arquivos. Para tentar resolver este problema
, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet,
ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser
feita através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal
'''
def conversao(b):
    m = 0
    m = b / (1024.0 * 1024.0)
    return m

def percentual(espaco, total):
    p = 0
    p = espaco / total
    return p  * 100

arquivo = open('usuarios-exerc02.txt','r')
linhas = arquivo.readlines()
arquivo.close()

usuarios = []
espacos = []
espacoTotal = 0
for l in linhas:
    linha = l.split()
    usuarios.append(linha[0])
    espacos.append(int(linha[1]))
espacoTotal = sum(espacos)

arquivo = open('relatorio-exerc02.txt','w')

arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários')
arquivo.write('------------------------------------------------------------------------')
arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso')

for i in range(0, len(usuarios)):
    c = conversao(espacos[i])
    espaco = percentual(espacos[i], espacoTotal);
    arquivo.write('%d %s           %.2f MB               %.2f%% \n' % ((i + 1), usuarios[i], c, espaco))

arquivo.write('Espaço total ocupado: %.2f MB' % (espacoTotal / (1024.0 * 1024.0)))
arquivo.write('Espaço médio ocupado: %.2f MB' % (espacoTotal / len(usuarios) / (1024.0 * 1024.0)))
arquivo.close()
