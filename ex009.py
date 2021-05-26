# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))
print('--' * 6)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))
print('--' * 6)