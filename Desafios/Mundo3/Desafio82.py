lista = []
lista2 = []
lista3 = []
while True:
    n = lista.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continua == 'S':
        lista.append(int(input('Digite um valor: ')))
        continua = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if continua == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista2.append(v)
    elif v % 2 != 0:
        lista3.append(v)
print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares foram: {lista2}')
print(f'Os valores impares foram: {lista3}')
