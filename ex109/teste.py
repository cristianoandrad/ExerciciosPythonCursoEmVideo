'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
nformando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from ex109 import moeda
# import moeda # ou este

p = float(input('Digite o preço: R$ '))
print(f'Aumentar 10% de {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}')
print(f'Diminuir 10% de {moeda.moeda(p)} é {moeda.diminuir(p, 10, True)}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
