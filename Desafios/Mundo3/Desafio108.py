from uteis.moedas import valores, valormonetario
n = float(input('Digite um numero: '))
a = float(input('Digite o acrescimo: '))
r = float(input('Digite o decrescimo: '))
print(f'O aumento de {valormonetario.monetario(n)} em {a}% é: {valormonetario.monetario(valores.aumentar(n, a))}')
print(f'A redução do valor {valormonetario.monetario(n)} em {r}% é: {valormonetario.monetario(valores.diminuir(n, r))}')
print(f'O dobro de {valormonetario.monetario(n)} é {valormonetario.monetario(valores.dobro(n))}')
print(f'A metade de {valormonetario.monetario(n)} é {valormonetario.monetario(valores.metade(n))}')
