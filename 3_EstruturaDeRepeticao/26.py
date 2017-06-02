'''
26. Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

candidato1 = 0
candidato2 = 0
candidato3 = 0

n = int(input('Entre com a quantidade de eleitores: '))

for i in range(1, n + 1):
    print('%d eleitor' % i)
    print('Digite 1-Candidato1, 2-Candidato2, 3-Candidato3')
    voto = int(input('Digite seu voto: '))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print('Candidato 1 teve %d votos' %candidato1)
print('Candidato 2 teve %d votos' %candidato2)
print('Candidato 3 teve %d votos' %candidato3)
    
        
            
        




    





    


    



