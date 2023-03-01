from uteis.moedas.valormonetario import monetario
def aumentar(n, a, money=False):
    p = (n * a)/100
    if money == True:
        return monetario(p + n)
    return p + n


def diminuir(n, d, money=False):
    p = (n * d)/100
    if money == True:
        return monetario(n - p)
    return n - p


def dobro(n, money=False):
    d = n * 2
    if money == True:
        return monetario(d)
    return d


def metade(n, money=False):
    m = n /2
    if money == True:
        return monetario(m)
    return m