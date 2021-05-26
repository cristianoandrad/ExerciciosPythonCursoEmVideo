#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

r = float(input('Digite um número inteiro: '))
#import math
from math import trunc
#print('O número {} tem a parte Inteira {}.'.format(r, math.floor(r)))
print('O número {} tem a parte Inteira {}.'.format(r, trunc(r)))
