def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda='R$'):
    return f'{moeda} {preço:>8.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=10):
    print('-' * 31)
    print('Resumo do valor'.center(31))
    print('-' * 31)
    print(f'Preço analizado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 31)


