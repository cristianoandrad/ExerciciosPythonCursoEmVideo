# Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao sem considerar espaços.
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
nomesplit = nome.split()
nomejoin = ''.join(nomesplit)
prinome = nomesplit[0]
print('O nome com todas as letras maiusculas:', nome.upper())
print('O nome com todas as letras minusculas:', nome.lower())
print('Quantidade de letras sem o espaço:',len(nomejoin))
print('O primeiro nome tem {} letras'.format(len(prinome)))
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} lebras.'.format(nome.find(' ')))
