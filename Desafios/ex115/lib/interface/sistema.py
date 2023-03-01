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

def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m-\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mSua Opção: \033[m')
    while opc < 1 or opc > 3:
        print('\033[31mDigite dentre as opções.\033[m')
        opc = leiaint('Sua Opção: ')
    return opc
