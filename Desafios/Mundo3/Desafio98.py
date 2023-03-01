from time import sleep
def contador():
    print('=' * 50)
    print('Contagem de 1 a 10!')
    for i in range(1, 11):
        print(i, end=' ')
        sleep(0.5)
    print('FIM!')
    print()
    print('=' * 50)
    print('Contagem de 10 a 0!')
    for d in range(10, -1, -2):
        print(d, end=' ')
        sleep(0.5)
    print('FIM!')
    print()
    print('=' * 50)
    print('AGORA SUA VEZ DE PERSONALIZAR A CONTAGEM:'.center(50))
    ini = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {ini} a {fim} em intervalo de {passo} em {passo}!')
    if fim > ini:
        for p in range(ini, fim+1, passo):
            print(p, end=' ')
            sleep(0.5)
    elif ini > fim:
        for p in range(ini, fim-1, -passo):
            print(p, end=' ')
            sleep(0.5)
    print('FIM!')
contador()
