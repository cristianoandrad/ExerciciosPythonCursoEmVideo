'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

perg = produto = nomebarato = ' '
total = barato = c = 0
custo1000 = 0
print('--' * 15)
print('{:^30}'.format('Loja Super Baratão'))
print('--' * 15)
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto R$: '))
    perg = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    c += 1
    while perg not in 'SN':
        perg = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    total += preco
    if c == 1 or preco < barato:
        barato = preco
        nomebarato = produto
    if preco >= 1000:
        custo1000 += 1
    if perg == 'N':
        break
print('{:=^30}'.format(' Fim do Programa '))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {custo1000} produtos que custaram mais de R$ 1.000,00')
print(f'O produto mais barato foi o {nomebarato} por R$ {barato:.2f}')
