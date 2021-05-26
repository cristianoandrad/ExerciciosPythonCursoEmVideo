#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' Lojas Guanabara '))
valor = float(input('Digite o valor o do produto: '))
forpag = int(input('Digite 1 p/ à vista dinheiro/cheque - 10% de desconto;\n'
                   'Digite 2 p/ à vista no cartão - 5% de desconto; \n'
                   'Digite 3 p/ parcelado em 2X no cartão - preço normal; \n'
                   'Digite 4 p/ parcelado em 3X ou mais no cartão - 20% de juros; \n'
                   'Codigo: '))
if forpag == 1:
    pag = valor - ((valor * 10) / 100)
elif forpag == 2:
    pag = valor - ((valor * 5) / 100)
elif forpag == 3:
    pag = valor
    parcela = pag / 2
    print('A parcela de 2x no cartão R$ {:.2f}'.format(parcela))
elif forpag ==4:
    pag = valor + ((valor * 20) / 100)
    qparcela = int(input('Digite a quantidade de parcelas: '))
    pagtotal= pag / qparcela
    print('A pacelado em {} no cartão ficará R$ {:.2f}'.format(qparcela, pagtotal))
else:
    pag = 0
    print('Opção inválida de pagamento')
print('O valor do produto ficará em R$ {:.2f}'.format(pag))
