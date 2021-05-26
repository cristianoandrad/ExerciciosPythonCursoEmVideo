'''Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.'''

from ex108 import moeda
# import moeda # ou este

p = float(input('Digite o preço: R$ '))
print(f'Aumentar 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuir 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 10))}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
