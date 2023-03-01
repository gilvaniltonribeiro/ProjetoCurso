tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
          'Athletico PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
          'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba',
          'Cuiabá-MT', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Os 5 primeiros colocados são {tabela[0:5]}')
print('='*30)
print((f'Os 4 ultimos colocados são {tabela[-4:]}'))
print('='*30)
print(f'Os times em ordem alfabetica:\n {sorted(tabela)}')
print('='*30)
print(f'O time {tabela[7]} esta na {tabela.index("Fortaleza")+1}° posição')
