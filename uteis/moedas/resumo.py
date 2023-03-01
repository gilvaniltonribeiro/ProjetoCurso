from uteis.moedas import valores
def resumo(n=0, a=0, r=0):
    print('='*50)
    print('RESUMO'.center(50))
    print('='*50)
    print(f'{"Preço analisado:":<} \t{valores.monetario(n):>50}')
    print(f'{"Dobro do preço:":<} \t{valores.dobro(n, True):>50}')
    print(f'{"Metade do preço:":<} \t{valores.metade(n, True):>50}')
    print(f'{f"{a}% Aumento:":<} \t\t{valores.aumentar(n, a, True):>50}')
    print(f'{f"{r}% Redução:":<} \t\t{valores.diminuir(n, r, True):>50}')
    print('='*50)
