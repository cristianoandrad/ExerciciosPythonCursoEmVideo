'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogadores = dict()
gols = list()
tot = 0
jogadores['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))
for g in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {g}? ')))
jogadores['gols'] = gols[:]
for t in gols:
    tot += t
jogadores['total'] = tot
#jogadores['total'] = sum(partidas) #  ou o for acima
print('-=-' * 20)
print(jogadores)
print('-=-' * 20)
for k, v in jogadores.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {jogadores["nome"]} jogou {len(jogadores["gols"])} partidas ')
for i, g in enumerate(jogadores["gols"]):
    print(f'=> Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogadores["total"]} gols')


