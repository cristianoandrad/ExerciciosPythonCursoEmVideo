'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''

palavras = ('aprender', 'programar', 'linguagens', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras: # p vai fazer a varredura em palavras
    print(f'\nNa palabra {p} temos ', end='')
    for letra in p: # letra vai fazer a varredura em p
        if letra in 'aeiou':
            print(letra, end=' ')
