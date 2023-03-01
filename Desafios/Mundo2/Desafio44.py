from time import sleep
valor = float(input('Digite o valor do produto: R$'))
print(('-'*10) + 'METODOS DE PAGAMENTO'.center(50, '-') + ('-'*10))
print('[1] À vista DINHEIRO/CHEQUE: 10% de DESCONTO')
print('[2] À vista no CARTAO: 5% de DESCONTO')
print('[3] Em até 2x no CARTAO: preço NORMAL')
print('[4] 3x ou mais no CARTAO: 20% de JUROS')
print('-'*70)
metodo = str(input('Digite o número corresponde para sua condição de pagamento: \n'))
parcela = int(input('Quantas parcelas?'))
print(('-'*10) + 'PROCESSANDO'.center(50, '-') + ('-'*10))
sleep(2)
print('....')
sleep(1)
print('.......')
sleep(1)
print('..........')
sleep(1)
if metodo == '1':
    print('O valor a ser pago é: R${:.2f}'.format(valor - (10/100 * valor)))
elif metodo == '2':
    print('O valor a ser pago é R${:.2f}'.format(valor - (5/100 * valor)))
elif metodo == '3':
    print('Duas parcelas de R${:.2f}'.format(valor/2))
elif metodo == '4':
    if parcela <= 2:
        print('Em {} parcelas de R${:.2f}'.format(parcela, valor / 2))
        print('Sua compra de R${:.2f} ficará no final R${:.2f}'.format(valor, valor))
    juros = ((20/100 * valor) + valor) / parcela
    dif = (20/100 * valor) + valor
    if parcela >= 3:
        print('Em {} parcelas de R${:.2f}'.format(parcela, juros))
        print('Sua compra de R${:.2f} ficará no final R${:.2f}'.format(valor, dif))
else:
    print('Tente novamente seguindo os passos adequados.')
