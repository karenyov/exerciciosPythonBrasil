'''
40. Foi feita uma estatística em cinco cidades brasileiras para coletar
dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a
que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos
de 2.000 veículos de passeio.
'''

maiorAcidente = 0
maiorAcidenteCidade = 0

menorAcicendte = 0
menorAcidenteCidade = 0

somaVeiculos = 0
somaAcidentes = 0
countAcicentes = 0
for i in range(1, 6):
    codigo = int(input('Digite o código da cidade: '))
    veiculos = int(input('Digite o número de veículos de passeio(em 1999): '))
    acidentes = int(input('Digite o número de acidentes de trânsito com vítimas(em 1999): '))

    if i == 1:
        menorAcidente = acidentes
        menorAcidenteCidade = codigo
        
    if acidentes > maiorAcidente:
        maiorAcidente = acidentes
        maiorAcidenteCidade = codigo
        
    if acidentes < menorAcidente:
        menorAcidente = acidentes
        menorAcidenteCidade = codigo

    somaVeiculos += veiculos

    if veiculos < 2000:
        somaAcidentes += acidentes
        countAcicentes += 1

print('Maior índice de acidentes de trânsito')
print('%d acidentes na cidade %d' %(maiorAcidente, maiorAcidenteCidade))

print('Menor índice de acidentes de trânsito')
print('%d acidentes na cidade %d' %(menorAcidente, menorAcidenteCidade))

print('Média de veículos das cinco cidades: %.2f' %(somaVeiculos/5))
print('média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: %.2f' %(somaAcidentes/countAcicentes))
    
