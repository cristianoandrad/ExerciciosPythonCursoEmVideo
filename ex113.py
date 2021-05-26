def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, por favor, digite um número válido')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar os dados')
            return 0
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'Voce acabou de digitar o numero {num}')