r1 = float(input('Digite primeira reta'))
r2 = float(input('Digite a segunda reta'))
r3 = float(input('Digite a terceira reta'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo!')
    if r1 == r2 == r3:
        print('O triangulo formado será Equilatero')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r1 != r3 or r2 == r3 != r1 or r3 == r1 != r2 or r3 == r2 != r1:
        print('O triangulo formado será Isosceles')
    elif r1 != r2 != r3 != r1:
        print('O triangulo formado será Escaleno')

else:
    print('Não pode formar um triangulo!')
