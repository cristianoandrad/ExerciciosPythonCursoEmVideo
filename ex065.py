# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

r = ''
soma = media = maior = menor = c = 0
while r != 'N':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if c == 1: # melhor forma de inicializar variável menor e maior
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / c
print('A media entre {} números foi {:.2f}'.format(c, media))
print('O maior é {} e o menor é {}'.format(maior, menor))
