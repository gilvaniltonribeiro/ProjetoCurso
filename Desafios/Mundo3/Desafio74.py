from random import randint
aleat = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {aleat}')
print(f'O maior valor entre os sorteados foi: {max(aleat)}')
print(f'O menor valor entre os sorteados foi: {min(aleat)}')
