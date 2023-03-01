matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for n in range(0, 3):
    for l in range(0, 3):
        matriz[n][l] = int(input(f'Digite um valor para {n}, {l}: '))
for n in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[n][l]:^5}]', end='')
    print()
