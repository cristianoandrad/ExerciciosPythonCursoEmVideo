# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite um algulo qualquer: '))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}, coseno {:.2f} e tangente de {:.2f}'.format(ang, seno, coseno, tangente))
