#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Digite a quantidades de dias com o carro: '))
km = float(input('Digite a quantidade de km percorrido: '))
print('Voce deve pagar R$ {:.2f} pelo aluguel do carro'.format((km * 0.15) + (dias * 60)))
