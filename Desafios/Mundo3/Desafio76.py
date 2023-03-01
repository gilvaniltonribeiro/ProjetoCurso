listagem = ('Lapis', 2, 'Borracha', 5, 'Caneta', 3, 'Mochila', 30, 'Mesa', 25)
print('=' * 50)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('=' * 50)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 != 0:
        print(f'R${listagem[pos]:>10.2f}')
print('=' * 50)
