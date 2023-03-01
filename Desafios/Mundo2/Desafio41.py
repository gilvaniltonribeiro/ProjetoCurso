from datetime import date
nasci = int(input('Digite seu ano de nascimento:'))
ano = date.today().year
idade = ano - nasci
if idade <= 9:
    print('O atleta tem {} anos'.format(idade))
    print('Categoria MIRIM')
elif 9 <= idade < 14:
    print('O atleta tem {} anos'.format(idade))
    print('Categoria INFANTIL')
elif 14 <= idade < 19:
    print('O atleta tem {} anos'.format(idade))
    print('Categoria JUNIOR')
elif 19 <= idade < 25:
    print('O atleta tem {} anos'.format(idade))
    print('Categoria SÊNIOR')
elif idade > 25:
    print('O atleta tem {} anos'.format(idade))
    print('Categoria MASTER')
