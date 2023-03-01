numeros = [[], []]
valor = 0
for p in range(1, 8):
    valor = (int(input(f'Digite o {p}° numero: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(f'Os valores digitados foram: {numeros}')
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
