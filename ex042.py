# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes

from time import sleep
a = float(input('Digite o primeiro do triangulo: '))
b = float(input('Digite o segundo do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))
print('-=-' * 20)
print('Analisando o triangulo')
print('-=-' * 20)
sleep(2)
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os seguimentos acima podem formar um triangulo ', end='')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('O triangulo não pode existir com essa medidas')
