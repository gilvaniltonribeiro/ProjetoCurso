pessoas = list()
pessoas2 = list()
pesadas = []
leves = []
maior = menor = 0
while True:
    pessoas2.append(str(input('Digite o nome: ')))
    pessoas2.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoas2[1]
    else:
        if pessoas2[1] > maior:
            maior = pessoas2[1]
        if pessoas2[1] < menor:
            menor = pessoas2[1]
    pessoas.append(pessoas2[:])
    pessoas2.clear()
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
for p in pessoas:
    if p[1] >= 70:
        pesadas.append(p[0])
    if p[1] <= 70:
        leves.append(p[0])
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso é {maior}Kg e as pessoas mais pesadas são{pesadas}')
print(f'O menor peso é {menor}Kg e as pessoas mais leves são{leves}')
