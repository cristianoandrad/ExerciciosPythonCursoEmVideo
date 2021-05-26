'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex107 import moeda
# import moeda # ou este

p = float(input('Digite o preço: R$ '))
print(f'Aumentar 10% de {p} é {moeda.aumentar(p, 10)}')
print(f'Diminuir 10% de {p} é {moeda.diminuir(p, 10)}')
print(f'Dobro de {p} é {moeda.dobro(p)}')
print(f'Metade de {p} é {moeda.metade(p)}')
