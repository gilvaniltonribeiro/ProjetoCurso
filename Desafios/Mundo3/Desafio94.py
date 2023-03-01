documentos = {}
ficha = []
soma = media = 0
while True:
    documentos.clear()
    documentos['Nome'] = str(input('Nome: '))
    while True:
        documentos['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if documentos['Sexo'] in 'MF':
            break
        print('ERRO. Digite apenas M OU F')
    documentos['Idade'] = int(input('Idade: '))
    soma += documentos['Idade']
    ficha.append(documentos.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]')).upper()[0]
        if continua in 'SN':
            break
        print('ERRO. Digite apenas S ou N')
    if continua == 'N':
        break
media = soma / len(ficha)
print(f'Foram registradas {len(ficha)} pessoas')
print(f'A media de idade {media:5.2f} das pessoas cadastradas')
print(f'As mulheres cadastradas foram', end=' ')
for p in ficha:
    if p["Sexo"] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'As pessoas com idade acima da media são: ', end=' ')
for c in ficha:
    if c["Idade"] >= media:
        print(f'{c["Nome"]}', end=' ')
print()
