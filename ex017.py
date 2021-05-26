# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o valor do cateto oposto do triângulo: '))
ca = float(input('Digite o valor do cateto adjacente do triângulo: '))
#hi = ((co**2)+(ca**2))**(1/2)
#hi = math.sqrt((co**2)+(ca**2))
hi = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
