'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as
quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

print('Digite 0 no código para sair')
print('Especifica código Preço')
while True:
    codigo = int(input('Digite o código: '))
    if codigo == 0:
        break
    quantidade = int(input('Digite a quantidade: '))

    if codigo == 100:
        print('Cachorro Quente %d %.2f' %(codigo, quantidade * 1.20))
    if codigo == 101:
        print('Bauru Simples %d %.2f' %(codigo, quantidade * 1.30))

    if codigo == 102:
        print('Bauru com ovo %d %.2f' %(codigo, quantidade * 1.50))

    if codigo == 103:
        print('Hambúrguer %d %.2f' %(codigo, quantidade * 1.20))

    if codigo == 104:
        print('Cheeseburguer %d %.2f' %(codigo, quantidade * 1.30))

    if codigo == 105:
        print('Refrigerante %d %.2f' %(codigo, quantidade * 1.00))
        
    
