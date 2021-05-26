# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite o valor em metros: '))
print('O valor digitado é {}dm {:0f}cm e {:0f}mm'.format(n * 10, n * 100, n * 1000))
