n = int(input('Digite um numero: '))
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero: '))
print('Foram digitados {} numeros e a soma entre eles é {}'.format(cont, soma))
