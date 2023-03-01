lista = []
boletim = []
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2)/2
    boletim.append([nome, [nota1, nota2], media])
    continua = str(input('QUER CONTINUAR? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print('-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-'*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Notas de qual aluno? [999 interrompe]'))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
