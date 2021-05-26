'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    menu = int(input('''Qual operação você deseja fazer ?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Digite o código escolhido: '''))
    if menu < 1 or menu > 5:
        print('\nOpção inválida, tente novamente\n')
    elif menu == 1:
        print('\nA soma nos números {} e {} é {:.2f}\n'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('\nA multiplicação nos números {} e {} é {:.2f}\n'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('\nO maior número entre {} e {} é o {}\n'.format(n1, n2, n1))
        else:
            print('\nO maior número entre {} e {} é o {}\n'.format(n1, n2, n2))
    elif menu == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
print('Finalizando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('\nO Programa foi finalizado! ')
