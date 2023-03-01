print('[M] Masculino')
print('[F] Feminino')
sexo = str(input('Digite aqui M ou F: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. por favor informe seu sexo.')).upper().strip()
if sexo == 'M':
    print('Voce informou Masculino')
elif sexo == 'F':
    print('Voce informou Feminino')
