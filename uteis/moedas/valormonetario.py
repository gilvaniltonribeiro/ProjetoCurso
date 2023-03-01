def monetario(n=0, din='R$'):
    m = (f'{din}{n:>8.2f}'.replace('.', ','))
    return m
