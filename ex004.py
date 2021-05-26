# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo deste valor é', type(algo))
print('Só tem espaços ?', algo.isspace())
print('É um numero:', algo.isalnum())
print('É u alfabético ?', algo.isalpha())
print('É alfanumerico ?', algo.isalnum())
print('Esta em maiúsculas ?', algo.isupper())
print('Esta em minúsculas ?', algo.islower())
print('Está capitalizada ?', algo.istitle())
