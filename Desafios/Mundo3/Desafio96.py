def area(lar, comp):
    area1 = lar * comp
    print(f'A área de um terreno {lar}x{comp} é {area1}m²')
print('-' * 50)
print('CONTROLE DE TERRENO'.center(50))
print('-' * 50)
lar = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(lar, comp)
