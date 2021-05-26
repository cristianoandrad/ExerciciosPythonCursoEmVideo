'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(l, c):
    print(f'A área do seu terreno {l} x {c} é de {l * c}m².')


print('Controle de terrenos')
print('-' * 20)
lar = float(input('Largura (m): '))
com = float(input('Comprimento (m): '))
area(lar, com)
