n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {} \n a multiplicação é {} e \n divisão é {:.3f}'.format(s, m, d), end='')
print('O resto da dvisão é {} e potencia é {}'.format(di, e))
