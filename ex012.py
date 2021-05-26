#  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Digite o valor do produto: '))
print('O valor do prpduto com desconto é {:.2f}'.format(prod - (prod * 0.05)))

