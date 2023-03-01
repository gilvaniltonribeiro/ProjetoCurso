n = int(input('Digite um numero: '))
print('[S] para sim')
print('[N] para não')
continua = str(input('Deseja continuar digitando?')).upper()
soma = n
maior = n
menor = n
contador = 1
while continua == 'S':
    n = int(input('Digite um numero: '))
    continua = str(input('Deseja continuar digitando?')).upper()
    if continua == 'S':
        contador += 1
        soma += n
    if continua != 'S':
        contador += 1
        soma += n
        print('Acabou')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('A media entre os valores digitados é {}'.format(soma/contador))
print('O maior valor digitado é {} e o menor é {}'.format(maior, menor))
