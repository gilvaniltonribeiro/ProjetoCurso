s = contmil = menor = contmenor = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Preço: R$'))
    s += valor
    contmenor += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Vai continuar? [S/N]')).strip().upper()[0]
    if contmenor == 1 or valor < menor:
        menor = valor
        barato = nome
    if valor >= 1000:
        contmil += 1
    if continua == 'N':
        break
print(f'O total gasto na compra sera R${s:.2f}')
print(f'Na compra existem {contmil} produtos que custam mais de R$1000')
print(f'O nome do produto mais barato é {barato} que custa R${menor:.2f}')
