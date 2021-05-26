# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um numero para obter a tabuada: '))
print('-=-' * 4)
for c in range(1, 11):
    print('{} x {:>2} = {}'.format(n, c, n * c))
print('-=-' * 4)