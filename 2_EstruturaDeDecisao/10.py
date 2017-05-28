'''
10. Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou NNoturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.
'''

turno = input('Digite o turno M-matutino, V-vespentino ou N-Noturno: ').upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')
