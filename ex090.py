'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

sala = list()
alunos = dict()
i = k = v = 0
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(F'Media de {alunos["nome"]}: '))
if alunos['media'] < 5:
    alunos['situacao'] = 'reprovado'
elif alunos['media'] >= 7:
    alunos['situacao'] = 'aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situacao'] = 'reprovado'

print(alunos['media'])
sala.append(alunos.copy())

for i in sala:
    for k, v in i.items():
        print(f'- {k} é igual a {v}')


