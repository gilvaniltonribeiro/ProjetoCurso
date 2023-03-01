extenso = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero e saiba ele por extenso[0 a 20]: '))
    if n < 0 or n > 20:
        print('Tente novamente. De 0 a 20')
        n = int(input('Digite um numero e saiba ele por extenso[0 a 20]: '))
    if 0 <= n <= 20:
        print(f'Voce digitou o numero {extenso[n]}')
