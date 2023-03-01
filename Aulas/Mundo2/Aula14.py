n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        elif n % 2 != 0:
            impar += 1
print('Foi digitado {} valores pares'.format(par))
print('Foi digitado {} valores impares'.format(impar))
print('Acabou')
