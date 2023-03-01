from datetime import datetime
ano = datetime.today().year
documentos = dict()
while True:
    documentos['Nome'] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento: '))
    documentos['Idade'] = ano - nasc
    documentos['Carteira'] = int(input('Carteira de trabalho[Digite 0 caso não tenha]: '))
    if documentos['Carteira'] != 0:
        documentos['Ano de contratação'] = int(input('Ano de contratação: '))
        documentos['Salario'] = float(input('Salário: R$ '))
        documentos['Aposentadoria'] = documentos['Idade'] + (documentos['Ano de contratação'] + 35) - ano
    continua = str(input('Quer continuar cadastrando? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
for k, v in documentos.items():
    print(f'{k} tem o valor {v}')
