# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
menor = []
maior = []
for c in range(7):
    ano = int(input('Digite o ano de nascimento: '))
    if (date.today().year - ano) < 21:
        menor.append(ano)
    else:
        maior.append(ano)
print('{} pessoas nascidas em {} não atingiram a maioridade'.format(len(menor), menor))
print('{} pessoas nascidas em {} atingiram a maioridade'.format(len(maior), maior))
