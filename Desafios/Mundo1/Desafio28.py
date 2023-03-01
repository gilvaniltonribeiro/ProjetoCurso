n = int(input('Escolha um número de 0 a 5'))
import random
from time import sleep
rand = random.randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if n == rand:
    print('Parabéns você acertou!')
else:
    print('Errou...Eu pensei no numero {}'.format(rand))
