# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER



from datetime import date
from time import sleep
ano = int(input('Informe a data de nascimento do atleta: '))
cat = date.today().year - ano
print('-=-' * 20)
print('Processando a categoria')
print('-=-' * 20)
sleep(2)
if cat <= 9:
    print('Mirim')
elif cat >= 10 and cat <= 14:
    print('Infantil')
elif cat >=  15 and cat <= 19:
    print('Junior')
elif cat >= 18 and car <= 20:
    print('Sênior')
elif cat >= 21:
    print('Master')

