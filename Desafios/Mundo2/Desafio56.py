somador = 0
mais_velho = 0
contador = 0
nome_mais_velho = ''
for reg in range(0, 4):
    nome = str(input('Digite seu Nome: '))
    idade = int(input('Digite sua idade: '))
    somador += idade
    print('[1] Masculino')
    print('[2] Feminino')
    sexo = int(input('Informe seu sexo:'))
    if sexo == 1 and idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    if sexo == 2 and idade < 20:
            contador += 1
print('A média de idade das pessoas informadas é {}'.format(somador/4))
print('O homem mais velho tem {} e se chama {}'.format(mais_velho, nome_mais_velho))
print('Existem {} mulheres abaixo de 20 anos'.format(contador))
