import math
from time import sleep
valor_da_casa = float(input('Qual o valor pretende pagar no imóvel?R$'))
salario = float(input('Qual a sua renda fixa mensal?R$'))
anos = int(input('Em quantos anos pretende pagar seu imóvel?'))
mensal = (valor_da_casa / (anos * 12))
if mensal >= 30/100 * salario:
    print('PROCESSANDO...')
    sleep(3)
    print('O valor calculado a pagar seria \033[1;31m {:.2f} \033[1;31m mensal'.format(mensal))
    sleep(2)
    print('Porém sua mensalidade calculada excede o permitido com base em seu salário.')
    print('Portando o acesso ao empréstimo está \033[1;31m NEGADO \033[1;31m')
    sleep(2)

elif mensal < 30/100 * salario:
    print('PROCESSANDO...')
    sleep(3)
    print('Seu empréstimo foi \033[1;32m APROVADO! \033[1;32m')
    sleep(2)
    print('O valor a ser pago mensalmente será \033[4;32m R${:.2f} por mes em {} anos \033[4;32m'.format(mensal, anos))
    sleep(2)
