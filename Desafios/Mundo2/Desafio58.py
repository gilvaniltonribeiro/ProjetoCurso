from random import randint
contador = 1
jogo = randint(0, 10)
palpite = int(input('Adivinhe um numero entre 0 e 10: '))
while palpite != jogo:
    if palpite > jogo:
        palpite = int(input('Menos... tente novamente: '))
        contador += 1
    if palpite < jogo:
        palpite = int(input('Mais... tente novamente: '))
        contador += 1
if palpite == jogo:
    print('PARABENS VC ACERTOU. Foram necessarios {} palpites'.format(contador))
