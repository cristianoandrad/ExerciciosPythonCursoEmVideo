# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
from time import sleep
a = float(input('Digite o primeiro do triangulo: '))
b = float(input('Digite o segundo do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))
print('-=-' * 20)
print('Analisando o triangulo')
print('-=-' * 20)
sleep(2)
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('O triangulo pode existir com essa medias')
else:
    print('O triangulo não pode existir com essa medidas')
