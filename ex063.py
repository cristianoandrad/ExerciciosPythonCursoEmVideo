# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Digite um número para obter a sequencia de fibonacc: '))
t1 = 0
t2 = 1
print(t1, t2, end=' ')
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    c += 1
