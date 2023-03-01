cont18 = contM = contF = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar cadastrando? [S/N]')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contM += 1
    if sexo == 'F' and idade <= 20:
        contF += 1
    if continua == 'N':
        break
print(f'Foram registradas {cont18} pessoas maiores ou de 18 anos')
print(f'Foram registrados {contM} homens')
print(f'Foram registradas {contF} mulheres abaixo ou de 20 anos')
