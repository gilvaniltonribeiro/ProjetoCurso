valor1 = int(input('Digite um numero: '))
valor2 = int(input('Digite um numero: '))
valor3 = int(input('Digite um numero: '))
valor4 = int(input('Digite um numero: '))
tupla = (valor1, valor2, valor3, valor4)
print(f'Os valores digitados foram: {tupla}')
print(f'O numero 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print((f'O numero 3 foi digitado na {tupla.index(3)+1}° posição'))
print(f'Os valores pares digitados foram:', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
