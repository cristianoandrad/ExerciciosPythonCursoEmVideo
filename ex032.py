# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Coloque 0 para ano atual ou digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
div4 = ano % 4
div400 = ano % 400
ndiv100 = ano % 100
print(ano,div4, ndiv100, div400)

if div4 == 0 and ndiv100 != 0 or div400 == 0:
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto')
