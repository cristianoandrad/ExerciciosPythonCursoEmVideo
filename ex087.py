'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
l = c = soma = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}:]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(0, 3):
    soma3 += matriz[l][2]
    if maior <= matriz[1][l]:
        maior = matriz[1][l]
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'A soma de todos os pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda coluna é {maior}')
