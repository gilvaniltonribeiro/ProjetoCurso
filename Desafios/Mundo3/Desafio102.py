def fatorial(n, show=False):
    total = 1
    for f in range(n, 0, -1):
        total *= f
        if show == True:
            print(f, end=' ')
            if f > 1:
                print('x', end=' ')
            else:
                print('= ' f'{total}')
    if show == False:
        print(total)
numero = int(input('Digite o numero para ver o fatorial: '))
fatorial(numero, show=True)
