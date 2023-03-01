pt = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao'))
for c in range(pt, (razao*10-1)+pt, razao):
    print(c, end='-> ')
print('FIM')
