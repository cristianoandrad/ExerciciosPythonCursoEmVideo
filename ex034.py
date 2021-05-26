# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salario do funcionário: '))
if sal >= 1250.00:
    aum = sal * 1.10
    print('O salário com aumento ficará de {:.2f}'.format(aum))
else:
    aum2 = sal * 1.15
    print('O salário com aumento ficará de {:.2f}'.format(aum2))
