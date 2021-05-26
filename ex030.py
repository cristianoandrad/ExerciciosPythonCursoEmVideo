# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um numero qualquer: '))
div = n % 2
if div == 0:
    print('O número é par !')
else:
    print('O número é impar !')
