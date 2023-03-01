from uteis.moedas import valores, valormonetario
n = int(input('Digite um numero: '))
a = int(input('Digite o acrescimo: '))
r = int(input('Digite o decrescimo: '))
print(f'O aumento de {valormonetario.monetario(n)} em {a}% é: {(valores.aumentar(n, a, True))}')
print(f'A redução do valor {valormonetario.monetario(n)} em {r}% é: {(valores.diminuir(n, r, True))}')
print(f'O dobro de {valormonetario.monetario(n)} é {(valores.dobro(n, True))}')
print(f'A metade de {valormonetario.monetario(n)} é {(valores.metade(n, True))}')
