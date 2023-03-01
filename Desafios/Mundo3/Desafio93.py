registro = dict()
partidas = list()
registro['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {registro["Nome"]} jogou? '))
for g in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {g+1}° partida?')))
registro['Gols'] = partidas[:]
registro['Total'] = sum(partidas)
print('-'*30)
print(registro)
print('-'*30)
for k, v in registro.items():
    print(f'O campo {k} tem valor {v}')
print('-'*30)
print(f'O jogador {registro["Nome"]} jogou {len(registro["Gols"])} partidas')
for i, v in enumerate(partidas):
    print(f'Na {i+1}° partida fez {v} gols')
print(f'Foi um total de {registro["Total"]} gols')
