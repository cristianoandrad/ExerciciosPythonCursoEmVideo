'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
          'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama',
          'Sport Recife', 'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('-=-' * 30)
print(f'Lista de times do brasileirão {tabela}')
print('-=-' * 30)
print(f'Os 5 primeiros do são {tabela[0:5]}')
print('-=-' * 30)
print(f'Os quatro últimos são {tabela[-4:]}')
print('-=-' * 30)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('-=-' * 30)
print('O Chapecoense está na {}ª posição'.format(tabela.index('Chapecoense')+1))

