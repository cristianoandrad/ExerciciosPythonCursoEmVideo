'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: ')).strip()
trabalhador['nasc'] = int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Nº Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['idade'] = datetime.now().year - trabalhador['nasc']
    idadeaposentadoria = (trabalhador['contratacao'] + 35) - trabalhador['nasc']
    trabalhador['aposentadoria'] = idadeaposentadoria
print('-=-' * 15)
for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}.')





