# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
# ou from random import randint
nu = int(input('Tente descobrir um numero de 0 a 5: '))
nc = random.randint(0, 5)
print('-=-' * 20)
print('Processando')
print('-=-' * 20)
time.sleep(2)
if nu == nc:
    print('O computador escolheu {}, voce ganhou !'.format(nc))
else:
    print('O computador escolher {}, voce perdeu !'.format(nc))
