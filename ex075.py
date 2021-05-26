'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite um ultimo número: ')))
print(f'Voce digitou os valores {tupla}.')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu primeiro na posição {tupla.index(3)+1}.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
