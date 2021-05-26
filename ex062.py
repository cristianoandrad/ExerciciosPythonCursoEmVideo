# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

'''pg = ''
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
i = 9
while pg != 0:
    l = [p]
    a = p
    for c in range(0, i):
        a += r
        l.append(a)
    print(l)
    pg = int(input('Voce quer mais quantos novos termos: '))
    i = i + pg'''

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
pa = p
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(pa, end=' ')
        pa += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Fim')
print('Progressão com {} termos mostrados.'.format(total))


