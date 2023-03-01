lista = []
lista.append(int(input('Digite um valor: ')))
continua = (str(input('Quer continuar digitando?[S/N]'))).strip().upper()[0]
while continua == 'S':
    lista.append(int(input('Digite um valor: ')))
    continua = (str(input('Quer continuar digitando?[S/N]'))).strip().upper()[0]
    if continua == 'N':
        break
print(f' Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Foram digitados: {lista}')
if 5 in lista:
    print('O VALOR 5 esta na lista')
    