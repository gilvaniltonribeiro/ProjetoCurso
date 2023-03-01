acumulador = 0
contador = 0
for n in range(1, 500):
    if (n % 3) == 0:
            if n % 2 != 0:
                contador += 1
                acumulador += n
print('Os {} valores somados são {}'.format(contador, acumulador))
