'''
25. Faça um programa que faça 5 perguntas para uma pessoa
sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final
emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado
como "Inocente".
'''

print('Digite 1-SIM ou 0-Não')

a = int(input('Telefonou para a vítima? '))
b = int(input('Esteve no local do crime? '))
c = int(input('Mora perto da vítima? '))
d = int(input('Devia para a vítima? '))
e = int(input('Já trabalhou com a vítima? '))

respostas = a + b + c + d + e
if respostas == 2:
    print('Suspeita')
elif respostas >=3 and respostas <= 4:
    print('Cúmplice')
elif respostas == 5:
    print('Assassino')
else:
    print('Inocente')










