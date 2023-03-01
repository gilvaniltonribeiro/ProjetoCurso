from random import randint
lista = []
listadefi = []
jogos = int(input('Quantos jogos serão gerados? '))
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    listadefi.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando {jogos} jogos')
for i, l in enumerate(listadefi):
    print(f'Jogo {i+1}: {l}')
