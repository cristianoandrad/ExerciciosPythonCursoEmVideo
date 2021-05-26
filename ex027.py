# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Primeiro nome:', nome[0])
print('Segundo nome:', nome[len(nome)-1])
