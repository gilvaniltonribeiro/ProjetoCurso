'''filme = {'Titulo': 'Star Wars', 'Ano': '1977', 'Diretor': 'George Lucas'}
print(filme.keys()) #indice
print(filme.values()) #valor
print(filme.items()) #os dois
for k, v in filme.items():
    print(f'O {k} é {v}')'''
estado = dict()
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} {v}')
        