'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    while perg not in 'SN':
        perg = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros')
print(f'Lista dos valores em ordem decrescente {lista}.')
if 5 in lista:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')

