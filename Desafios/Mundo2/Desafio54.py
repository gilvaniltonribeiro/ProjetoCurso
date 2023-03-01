from datetime import date
ano = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nas = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    idade = ano - nas
    if idade >= 18:
        totalmaior += 1
    elif idade < 18:
        totalmenor += 1
print('Existem {} maiores'.format(totalmaior))
print('Existem {} menores'.format(totalmenor))
