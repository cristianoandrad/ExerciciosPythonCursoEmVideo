# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize
print('-=-' * 14)
print('{:=^42}'.format(' Contagem Regressiva '))
print('-=-' * 14)
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print(emojize('Fogos ! :collision:'))

