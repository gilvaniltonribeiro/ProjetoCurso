from random import randint
numeros = []
def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os numeros sorteados foram {lista}')
def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos pares é {soma}')
sorteia(numeros)
somaPar(numeros)
