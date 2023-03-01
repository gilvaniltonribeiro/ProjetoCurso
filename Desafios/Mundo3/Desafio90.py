boletim = dict()
boletim['Nome'] = str(input('Digite o Nome: '))
boletim['Media'] = float(input('Digite a media: '))
if boletim['Media'] >= 7:
        boletim["Situação"] = 'Aprovado'
elif 5 <= boletim['Media'] < 7:
    boletim["Situação"] = 'Recuperação'
else:
    boletim["Situação"] = 'Reprovado'
for k, v in boletim.items():
        print(f'{k} é igual {v}')
