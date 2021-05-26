# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
s = v = 0
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)
while True:
    nu = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    nc = randint(0, 10)
    s = nu + nc
    if s % 2 == 0:
        print('---' * 10)
        print(f'Você jogou {nu} e o computador {nc}. Total de {s} deu par')
        print('---' * 10)
        if pi == 'P':
            print('Voce venceu !')
            print('Vamor jogar novamente ...')
            print('-=-' * 10)
            v += 1
        else:
            print(f'Voce perdeu - Gamer Over, você venceu {v} vezes!')
            print('-=-' * 10)
            break
        print()
    else:
        print('---' * 10)
        print(f'Você jogou {nu} e o computador {nc}. Total de {s} deu impar')
        print('---' * 10)
        if pi == 'I':
            print('Voce venceu !')
            print('Vamor jogar novamente ...')
            print('-=-' * 10)
            v += 1
        else:
            print(f'Voce perdeu - Gamer Over, você venceu {v} vezes!')
            print('-=-' * 10)
            break
