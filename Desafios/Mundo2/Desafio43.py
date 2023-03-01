altura = float(input('Digite sua altura: (m)'))
peso = float(input('Digite seu peso: (Kg)'))
formula = peso / (altura * altura)
IMC = round(formula, 1)
if IMC < 18.5:
    print('O IMC desta pessoa é {}'.format(IMC))
    print('ABAIXO DO PESO')
elif 18.5 <= IMC < 25:
    print('O IMC desta pessoa é {}'.format(IMC))
    print('PESO IDEAL')
elif 25 <= IMC < 30:
    print('O IMC desta pessoa é {}'.format(IMC))
    print('SOBREPESO')
elif 30 <= IMC < 40:
    print('O IMC desta pessoa é {}'.format(IMC))
    print('OBESIDADE')
elif IMC >= 40:
    print('O IMC desta pessoa é {}'.format(IMC))
    print('OBESIDADE MORBIDA')
else:
    print('Are you a ghost?')
