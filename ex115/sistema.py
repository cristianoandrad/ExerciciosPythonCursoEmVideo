from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabecario('Sistema Arquivo v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecario('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecario('Saindo do sistema... Até Logo')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)