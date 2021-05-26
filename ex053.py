# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.


frase = str(input('Digite uma frase: ')).strip().lower()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
#inverso = junto[::-1] #substitui o for
for letra in range(len(juntar)-1, -1, -1):
    inverso += juntar[letra]
print('O inverso de {} é {}'.format(juntar, inverso))
if juntar == inverso:
    print('É palindromo')
else:
    print('Não é palindromo', inverso)
