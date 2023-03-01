from uteis.moedas.leiadinheiro import leitura
from uteis.moedas.ex111.resumo import resumo
p = leitura('Digite o preço:R$ ')
a = leitura('Digite a porcentagem de aumento: ')
r = leitura('Digite a porcentagem redução: ')
resumo(p, a, r)
