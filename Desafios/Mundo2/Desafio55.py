maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: Kg'.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
