km = float(input('Informe a velocidade do seu carro'))
multa = km - 80
if km>80:
    print('Você foi multado! E deverá pagar R${:.2f}'.format(multa * 7))
else:
    print('Parabéns voce andou na velocidade adequada e não pagará multa.')
