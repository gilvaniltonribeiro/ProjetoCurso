valor = []
while True:
    v = int(input('Digite o valor: '))
    if v not in valor:
        valor.append(v)
    else:
        print('Valor duplicado. Nao vou adicionar')
    continua = str(input('Quer continuar digitando? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
valor.sort()
print(valor)
