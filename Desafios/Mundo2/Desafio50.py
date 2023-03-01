soma = 0
for n in range(1, 7):
    num = int(input('Digite o {}° valor'.format(n)))
    if (num % 2) == 0:
        soma += num
print('Os valores somados são {}'.format(soma))
