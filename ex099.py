'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(* numeros):
    m = c = 0
    print('-=-' * 20)
    print('Analisando os valores passados...')
    for n in numeros:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
        if c == 0:
            m = n
        else:
            if n > m:
                m = n
        c += 1
    print(f'\nForam informados {c} valores ao todo')
    print(f'O maior valor informado foi {m}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)



