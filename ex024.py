# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cid = str(input('Digite o nome da cidade: ')).strip().upper()
div = cid.split()
print(cid)
print('A cidade começa com o nome Santo? ', 'SANTO' in div[0])
print(cid[:5] == 'SANTO')
