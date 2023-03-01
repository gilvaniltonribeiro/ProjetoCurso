sal = float(input('Qual seu salário?R$'))
if sal > 1250:
    print('Seu salário com aumento será R${:.2f}'.format(sal + (10/100 * sal)))
else:
    print('Seu salário com aumento será R${:.2f}'.format(sal + (15/100 * sal)))
