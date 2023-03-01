km = float(input('Qual a distância percorrida?Km'))
print('Você esta prester a começar uma viagem de {:.1f}Km'.format(km))
if km<=200:
    print('E o preço a pagar pela viagem será R${:.2f}'.format(km * 0.50))
else:
    print('E o preço a pagar pela viagem será R${:.2f}'.format(km * 0.45))
