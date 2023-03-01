Km = float(input('Quantos Km percorridos?'))
D = int(input('E quantos dias alugado?'))
pago = (Km * 0.15) + (D * 60)
print('O total a pagar é de R${:.2f}'.format(pago))
