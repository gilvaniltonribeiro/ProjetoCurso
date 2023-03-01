n = int(input('Digite qualquer número e saiba se é par ou impar'))
resultado = n % 2
if resultado == 1:
    print('O número {} é IMPAR'.format(n))
else:
    print('O número {} é PAR'.format(n))
