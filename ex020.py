# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
alu1 = str(input('Digite o nome do aluno: '))
alu2 = str(input('Digite o nome do aluno: '))
alu3 = str(input('Digite o nome do aluno: '))
alu4 = str(input('Digite o nome do aluno: '))
alunos = [alu1, alu2, alu3, alu4]
shuffle(alunos)
print('A ordem dos alunos será {}'.format(alunos))
