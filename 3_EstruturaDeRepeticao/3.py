'''
3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    nome = input('Digite seu nome: ')
    if len(nome) > 3:
        break
    else:
        print('Digite novamente.')

while True:
    idade = int(input('Digite sua idade: '))
    if idade > 0 and idade <= 150:
        break
    else:
        print('Digite novamente.')
        
while True:
    salario = float(input('Digite seu salário: '))
    if salario >= 0:
        break
    else:
        print('Digite novamente.')

while True:
    sexo = input('Digite seu sexo(F-feminino ou M-masculino): ').upper()
    if sexo in 'FM':
        break
    else:
        print('Digite novamente.')

while True:
    estado = input('Digite seu estado civil(S-solteito, C-casado, V-Viúvo, D-divorciado): ').upper()
    if estado in 'SCVD':
        break
    else:
        print('Digite novamente.')

    



