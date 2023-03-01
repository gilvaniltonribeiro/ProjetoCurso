def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO.Por favor digite um numero valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO.Por favor digite um numero valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


n1 = leiafloat('Digite um real: ')
n2 = leiaint('Digite um inteiro: ')
print(f'Voce digitou o numero inteiro {n2} e o real {n1}')
