cidade = str(input('Digite sua Cidade')).strip()
print(cidade[:5].upper() == 'SANTO')
print('Sua cidade começa com Santo?{}'.format('SANTO' in cidade.upper()))
