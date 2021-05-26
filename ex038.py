# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O numero {} é o maior'.format(n1))
elif n2 > n1:
    print('O numero {} é o maior'.format(n2))
else:
    print('Os dois numeros são iguais')
