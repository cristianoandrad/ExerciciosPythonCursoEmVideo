# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
l = []
for c in range(0, 6):
    n = int(input('Digite numero {}: '.format(c + 1)))
    if (n % 2) == 0:
        s += n
        l.append(n)
print('A Soma de {} resulta em {}.'.format(l, s))
