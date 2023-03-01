r1 = float(input('Digite primeira reta'))
r2 = float(input('Digite a segunda reta'))
r3 = float(input('Digite a terceira reta'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')
