'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
na = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Listagem dos números: ', end='')
for n in na:
    print(n, end=' ')
print('\nMenor número:', min(na))
print('Maior número:', max(na))

