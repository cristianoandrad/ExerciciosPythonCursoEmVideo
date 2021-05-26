'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista.'''

n = []
maior = menor = 0
for i in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = n[i]
    else:
        if n[i] > maior:
            maior = n[1]
        if n[i] < menor:
            menor = n[i]
print('-=-' * 30)
print(f'Você digitou os valores {n}.')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, e in enumerate(n):
    if e == maior:
        print(p, end='..')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p, e in enumerate(n):
    if e == menor:
        print(p, end='..')
