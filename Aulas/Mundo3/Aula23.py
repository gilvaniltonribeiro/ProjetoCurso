try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = n / d
except (ValueError, TypeError):
    print(f'\033[0;31mInfelizmente tivemos um erro com os dados\033[m')
except (ZeroDivisionError):
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')
