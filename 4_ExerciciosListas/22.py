'''
22 -
Sua organização acaba de contratar um estagiário para trabalhar no
Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área.
A primeira tarefa dele é testar todos
os cerca de 200 mouses que se encontram lá, testando e anotando o estado
de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber um número indeterminado de entradas,
cada uma contendo: um número de identificação do mouse o tipo de defeito:

necessita da esfera;
necessita de limpeza;
a.necessita troca do cabo ou conector;
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

problemas = [0] * 4
print('''1- necessita da esfera
2- necessita de limpeza
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado ''')
while True:
    identificacao = int(input('Identificação: '))
    if identificacao == 0:
        break
    problema = int(input('Digite o número do problema: '))
    problemas[problema - 1] = problemas[problema - 1] + 1
                
print('Situação                        Quantidade              Percentual')
total = sum(problemas)
print('1- necessita da esfera                  %d              %.2f' % (problemas[0],  (100 * problemas[0]) / total))
print('2- necessita de limpeza                 %d              %.2f' % (problemas[1], (100 * problemas[1]) / total))
print('3- necessita troca do cabo ou conector  %d              %.2f' % (problemas[2], (100 * problemas[2]) / total))
print('4- quebrado ou inutilizado              %d              %.2f' % (problemas[3], (100 * problemas[3]) / total))
    
    
