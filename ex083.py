'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

'''frase = str(input('Digite uma expressão qualquer: '))
list1 = list()
list2 = list()
for i in frase:
    if i == '(':
        list1.append(i)
    if i == ')':
        list2.append(1)
if len(list1) == len(list2):
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')'''

expr = str(input('Digite sua expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta')
else:
    print('Sua expressão esta errada')


