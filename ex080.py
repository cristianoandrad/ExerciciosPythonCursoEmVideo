'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

numeros = list()
for i in range(0, 5):
    n = int(input('Digite um número: '))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print('Adicionado na posição: ', pos)
                break
            pos += 1
print('Os valores digitados foram', numeros)


