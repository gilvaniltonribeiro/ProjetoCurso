from random import randint
print('Jogue par ou impar')
n = int(input('Escolha um numero: '))
escolha = str(input('PAR ou IMPAR[P/I]')).strip().upper()[0]
pc = randint(0, 999)
soma = pc + n
cont = 0
while soma % 2 == 0 or soma != 0:
    if soma % 2 == 0 and escolha == 'P':
        print('Voce GANHOU. FOI PAR')
        print(f'O computador escolheu {pc} e voce {n}, resultando em {soma}')
        cont += 1
        pc = randint(0, 999)
        n = int(input('Escolha um numero: '))
        escolha = str(input('PAR ou IMPAR[P/I]')).strip().upper()[0]
        soma = pc + n
    if soma % 2 != 0 and escolha == 'I':
        print('VOCE GANHOU. FOI IMPAR')
        print(f'O computador escolheu {pc} e voce {n}, resultando em {soma}')
        cont +=1
        pc = randint(0, 999)
        n = int(input('Escolha um numero: '))
        escolha = str(input('PAR ou IMPAR[P/I]')).strip().upper()[0]
        soma = pc + n
    if soma % 2 == 0 and escolha == 'I':
        print('Voce PERDEU. FOI PAR')
        print(f'O computador escolheu {pc} e voce {n}, resultando em {soma}')
        break
    if soma % 2 != 0 and escolha == 'P':
        print('Voce PERDEU. FOI IMPAR')
        print(f'O computador escolheu {pc} e voce {n}, resultando em {soma}')
        break
print(f'O jogador conquistou {cont} vitorias consecutivas')
