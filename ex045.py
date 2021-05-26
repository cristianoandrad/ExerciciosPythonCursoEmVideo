# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time
print('-=-' * 20)
print('Jokenpo')
print('-=-' * 20)
jogador = int(input('Digite 1 p/ Pedra, 2 p/ Tesoura e 3 p/ Papel: '))
print('Jo')
time.sleep(0.5)
print('ken')
time.sleep(0.5)
print('pô')
pc = random.randint(1, 3)
if jogador == 1 and pc == 1:
    print('Empate, ambos escolheram Pedra!')
elif jogador == 2 and pc == 2:
    print('Empate, ambos escolheram Tesoura!')
elif jogador == 3 and pc == 3:
    print('Empate, ambos escolheram Papel !')
elif jogador == 1 and pc == 2:
    print('Voce ganhou \nO computador escolheu Tesoura \n E você escolheu Pedra!')
elif jogador == 2 and pc == 3:
    print('Voce ganhou \nO computador escolheu Papel \nE você escolheu Tesoura !')
elif jogador == 3 and pc == 1:
    print('Voce ganhou \nO computador escolheu Pedra \nE você escolheu Papel !')
elif jogador == 1 and pc == 3:
    print('Voce perdeu \nO computador escolheu Papel \nE você escolheu Tesoura!')
elif jogador == 2 and pc == 1:
    print('Voce perdeu \nO computador escolheu Pedra \nE você escolheu Papel!')
elif jogador == 3 and pc == 2:
    print('Voce perdeu \nO computador escolheu Tesoura \nE você escolheu Pedra!')
else:
    print('Opção inválida, tente novamnte')
