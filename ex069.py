'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

idade = idade18 = homens = mulheres20 = 0
sexo = perg = ''
while True:
    print('--' * 15)
    print('{:^30}'.format('Cadastre uma pessoa'))
    print('--' * 15)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('--' * 15)
    perg = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    while perg not in 'SN':
        perg = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres20 +=1
    if perg == 'N':
        break
print('{:=^30}'.format(' Fim do Programa '))
print(f'Total das pessoas com mais de 18 anos: {idade18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
