# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar
lat = area / 2
print('A parede tem {:.2f}m² e precisa de {:.0f} latas'.format(area, lat))
