# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome

nome = str(input('Digite o nome da pessoa: ')).strip()
mai = nome.upper()
print('O nome da pessoa tem Silva: ', 'SILVA' in mai)
