import random
from time import sleep
import emoji
print(('-'*10)+'Vamos jogar Jokenpô!'.center(50, '-')+('-'*10))
print('É muito simples...')
print('Escolha entre:')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
escolha = int(input(('-'*10)+'Escolha um objeto:'.center(50, '-')+('-'*10)))
pedra = '1'
papel = '2'
tesoura = '3'
lista = [pedra, papel, tesoura]
jogo = random.choice(lista)
print('JO...')
sleep(1)
print('KEN....')
sleep(1)
print('PÔ!!!')
sleep(1)
#pedra
if escolha == 1 and jogo == papel:
    print(emoji.emojize(':raised_hand: VOCÊ PERDEU! TENTE DE NOVO.'))
elif escolha == 1 and jogo == tesoura:
    print(emoji.emojize(':victory_hand: VOCÊ GANHOU! PARABÉNS!'))
elif escolha == 1 and jogo == pedra:
    print(emoji.emojize(':oncoming_fist: EMPATE. TENTE NOVAMENTE!'))
#papel
elif escolha == 2 and jogo == tesoura:
    print(emoji.emojize(':victory_hand: VOCÊ PERDEU! TENTE DE NOVO.'))
elif escolha == 2 and jogo == pedra:
    print(emoji.emojize(':oncoming_fist: VOCÊ GANHOU! PARABÉNS!'))
elif escolha == 2 and jogo == papel:
    print(emoji.emojize(':raised_hand: EMPATE. TENTE NOVAMENTE!'))
#tesoura
elif escolha == 3 and jogo == pedra:
    print(emoji.emojize(':oncoming_fist: VOCÊ PERDEU! TENTE DE NOVO.'))
elif escolha == 3 and jogo == papel:
    print(emoji.emojize(':raised_hand: VOCÊ GANHOU! PARABÉNS!'))
elif escolha == 3 and jogo == tesoura:
    print(emoji.emojize(':victory_hand: EMPATE. TENTE NOVAMENTE!'))
else:
    print('ALGO DEU ERRADO... TENTE NOVAMENTE')
