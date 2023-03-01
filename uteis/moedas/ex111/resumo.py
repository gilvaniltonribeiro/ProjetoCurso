from uteis.moedas import valores
def resumo(n, a, r):
    print('='*50)
    print('RESUMO'.center(50))
    print('='*50)
    print(f'{"Preço analisado:":<} {valores.monetario(n):>30}')
    print(f'{"Dobro do preço:":<} {valores.dobro(n, True):>30}')
    print(f'{"Metade do preço:":<} {valores.metade(n, True):>30}')
    print(f'{f"{a}% Aumento:":<} {valores.aumentar(n, a, True):>30}')
    print(f'{f"{r}% Redução:":<} {valores.diminuir(n, r, True):>30}')
