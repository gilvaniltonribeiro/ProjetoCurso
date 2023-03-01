pt = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao'))
pa = pt
contador = 1
while contador <= 10:
    print(pa, end='-> ')
    pa += razao
    contador += 1
print('Fim')
