'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''


'''print('--' * 15)
print('{:^30}'.format('Banco CEV'))
print('--' * 15)
valor = int(input('Qual o valor que você quer sacar R$ '))
c50 = valor % 50
c20 = c50 % 20
c10 = c20 % 10
c1 = c10 % 1
b50 = valor - c50
b20 = valor - b50 - c20
b10 = valor - b50 - b20 - c10
b1 = valor - b50 - b20 - b10 - c1
print(f'Total de {b50/50:.0f} celulas de R$ 50,00')
print(f'Total de {b20/20:.0f} celulas de R$ 20,00')
print(f'Total de {b10/10:.0f} celulas de R$ 10,00')
print(f'Total de {b1/1:.0f} celulas de R$ 1,00')
print('--' * 15)
print('Volte sempre ao Banco CEV! Tenha um bom dia')'''

'''valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")'''

print('--' * 15)
print('{:^30}'.format('Banco CEV'))
print('--' * 15)
valor = int(input('Qual o valor que você quer sacar R$ '))
total = valor
cel = 50
contCel = 0
while True:
    if total >= cel:
        total -= cel
        contCel += 1
    else:
        print(f'O total de {contCel} céluldas de R$ {cel}.')
        if cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        contCel = 0
        if total == 0:
            break



