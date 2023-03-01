from datetime import date
nascimento = int(input('Digite seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - nascimento
if idade == 18:
    print('Você tem {} anos e já esta no período de idade para se alistar ao serviço militar.'.format(idade))
elif idade > 18:
    print('Você com {} anos ja passou da idade de se alistar ao serviço militar, adiando {} anos'.format(idade, idade-18))
    print('Seu alistamento deveria ter sido em {}'.format(nascimento + 18))
else:
    print('Você tem ainda {} anos não tem a idade para se alistar, porém faltam {} anos.'.format(idade, 18 - idade))
    print('Seu alistamento será no ano de {}'.format(nascimento + 18))
