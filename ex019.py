#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
alu1 = str(input('Digite o primeiro aluno: '))
alu2 = str(input('Digite o segundo aluno: '))
alu3 = str(input('Digite o terceiro aluno: '))
alu4 = str(input('Digite o quarto aluno: '))
alunos = [alu1, alu2, alu3, alu4]
sorteio = choice(alunos)
print('O aluno sorteado foi {}.'.format(sorteio))
