n = int(input('Digite um número inteiro qualquer'))
print('Escolha a base de conversão:')
print('[1] Para binario')
print('[2] Para octal')
print('[3]- Para hexadecimal')
conversao = int(input('Digite a conversão escolhida:'))
if conversao == 1:
    print('O número {} em binário {}'.format(n, bin(n)[2:]))
elif conversao == 2:
    print('O número {} em octal {}'.format(n, oct(n)[2:]))
elif conversao == 3:
    print('O numero {} em Hexadecimal {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida.')
