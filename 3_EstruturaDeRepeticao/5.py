'''
5. Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''


a = float(input('Digite a quantidade da população a: '))
b = float(input('Digite a quantidade da população b: '))
anos = 0

while a <= b:
    a = (a + (a * 3) / 100)
    b = (b + (b * 1.5) / 100)
    anos += 1
    
print(anos)
    
    


    



