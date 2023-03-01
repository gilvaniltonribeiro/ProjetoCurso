valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print(('=' * 10) + 'MENU'.center(50, '=') + ('=' * 10))
    print('[1] SOMA')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('=' * 70)
    escolha = int(input(' '))
    if escolha == 1:
        resultado = valor1 + valor2
        print('O resultado é {}'.format(resultado))
    elif escolha == 2:
        resultado = valor1 * valor2
        print('O resultado é {}'.format(resultado))
    elif escolha == 3:
        if valor1 > valor2:
            print('O  numero {} é o maior'.format(valor1))
        if valor2 > valor1:
            print('O numero {} é o maior'.format(valor2))
        elif valor1 == valor2:
            print('Os valores são iguais.')
    elif escolha == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Finalizando programa...')
    else:
        print('Opção invalida. Tente novamente...')
