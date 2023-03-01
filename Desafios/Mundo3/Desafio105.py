def notas(*n, sit=False):
    '''
    -> função para analisar as notas:
    :param n: Inserir as notas
    :param sit: se False nao ira mostrar a situação e se True irá
    :return: Retorna a maior, menor, media e quantidade de notas assim como a situação.
    '''

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] <= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5, 6, 8.5, sit=True)
print(resp)
#help(notas)
