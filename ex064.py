# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = c = soma = 0
n = int(input('Digite os numeros para obter a soma [Parar com 999]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite os numeros para obter a soma [Parar com 999]: '))
print('Resultado das somas dos {} numeros foi {}'.format(c, soma))
