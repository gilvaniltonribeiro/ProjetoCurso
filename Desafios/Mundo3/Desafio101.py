def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 16 <= idade <= 17 or idade >= 70:
        return f'Com {idade} anos é opcional votar.'
    elif idade < 16:
        return f'Com {idade} anos não vota.'
    else:
        return f'Com {idade} anos o voto é obrigatorio.'
nasc = int(input('Seu ano de nascimento: '))
print(voto(nasc))
