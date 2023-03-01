nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO pois sua média foi {}'.format(media))

elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO pois sua média foi {}'.format(media))

elif media >= 7.0:
    print('APROVADO pois sua média foi {}'.format(media))
