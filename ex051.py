# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
l = [p]
a = p
for c in range(0, 9):
    a += r
    l.append(a)
print(l)
