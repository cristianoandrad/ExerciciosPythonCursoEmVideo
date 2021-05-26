# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anonasc = int(input('Digite o ano de seu nascimento para informação de alistamento militar: '))
anoatual = date.today().year
alista = anoatual - anonasc
tempo = 18 - alista
print('Quem nasceu em {} tem {} em {}'.format(anonasc, alista, anoatual))
if alista < 18:
    ano = anoatual + tempo
    print('Falta {} anos para se alistar em {}'.format(tempo, ano))
elif alista == 18:
        print('O alistamento é imediato !')
else:
    ano = anoatual + tempo
    print('Voce deveiria ter se alistado há {} anos em {}'.format(tempo * -1, ano))
