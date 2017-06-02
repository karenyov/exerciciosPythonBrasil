'''
15. A série de Fibonacci é formada pela
seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a
série até o n−ésimo termo.
'''

numero = int(input('Digita o número: '))
resultado = 0

primeiro = 0
print (primeiro)
segundo = 1

for i in range(1, numero):
    print(segundo, end=',')
    terceiro = primeiro + segundo
    primeiro, segundo = segundo, terceiro
    
    





    


    



