# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
numpc = randint(0, 10)
numus = int(input('Tente adivinhar um número de 0 a 10 que pensei: '))
vezes = 1
while numpc != numus:
    if numus < numpc:
        numus = int(input('É maior, tente novamente: '))
    else:
        numus = int(input('É menor, tente novamente: '))
    vezes += 1
print('Você acertou, pensei no numero {} e você no {}, conseguiu com {} palpites!'.format(numpc, numus, vezes))
