from uteis.moedas.valormonetario import monetario
def aumentar(n=0, a=0, money=False):
    p = n + (n * a)/100
    return p if money == False else monetario(p)


def diminuir(n=0, d=0, money=False):
    p = n - (n * d)/100
    return p if money == False else monetario(p)


def dobro(n=0, money=False):
    d = n * 2
    return d if money == False else monetario(d)


def metade(n=0, money=False):
    m = n /2
    return m if money == False else monetario(m)