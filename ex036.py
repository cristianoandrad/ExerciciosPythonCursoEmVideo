#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

vcasa = float(input('Digite o valor da casa: '))
salar = float(input('Digite o salario: '))
anosf = float(input('Digite quantos anos será o financiamento: '))
parcf = (vcasa / anosf) / 12
cap = (salar * 30) / 100
if parcf <= cap:
    print('O financiamento foi aprovado em {:.2f} anos no valor de  R$ {:.2f} com a parcela de R$ {:.2f} '.format(anosf, vcasa, parcf))
else:
    print('O valor não foi aprovado pois excede o limite de finaciamento, parcela em R$ {:.2f} !'.format(parcf))
