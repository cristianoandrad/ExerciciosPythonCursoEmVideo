# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro: '))
if vel > 80.0:
    multa = (vel - 80.0) * 7
    print('Voce foi multado em R$ {:.2f} por excesso de velocidade. '.format(multa))
else:
    print('Parabéns, você digite muito bem !')
