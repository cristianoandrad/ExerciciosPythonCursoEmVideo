lista = list()
pares = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    #if n % 2 == 0:
    #    pares.append(n)
    #else:
    #    impar.append(n)
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break
print(f'Lista dos números completa {lista}')
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impar.append(c)
print(f'Lista dos números pares {pares}')
print(f'Lista dos números impares {impar}')
