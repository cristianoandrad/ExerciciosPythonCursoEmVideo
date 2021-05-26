# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input('Digite a distância em km da viagem: '))
if km <= 200:
    pa = km * 0.5
    print('O preços da passagem custará R$ {:.2f}.'.format(pa))
else:
    pa2 = km * 0.45
    print('O preço da passagem custará R$ {:.2f}.'.format(pa2))

preco = km * 0.5 if km <=200 else km * 0.45 # simplificado
print('O preço da passagem será de {}'.format(preco))