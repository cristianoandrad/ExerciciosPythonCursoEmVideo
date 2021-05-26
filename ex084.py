'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista = list()
pessoas = list()
maispesadas = list()
maior = menor = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso foi de {menor}', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0])
