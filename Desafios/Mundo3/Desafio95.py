time = list()
registro = dict()
partidas = list()
while True:
    registro.clear()
    registro['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {registro["Nome"]} jogou? '))
    partidas.clear()
    for g in range(0, tot):
        partidas.append(int(input(f'Quantos gols na {g+1}° partida?')))
    registro['Gols'] = partidas[:]
    registro['Total'] = sum(partidas)
    time.append(registro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite apenas S ou N.')
    if resp == 'N':
        break
print('-'*50)
print('cod ', end='')
for i in registro.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end=' - ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO. NÃO EXISTE JOGADOR COM CODIGO {busca}')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]} --- ')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'No jogo {i+1} fez {g} gols')
    print('-'*50)
