pt = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao'))
mais = int(input('Quantos termos voce quer mostrar mais? '))
pa = pt
total = 0
contador = 1
while mais != 0:
    total = total + mais
    while contador <= total:
        print(pa, end='-> ')
        pa += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print('Fim')
