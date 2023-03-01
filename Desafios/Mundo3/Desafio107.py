from uteis.moedas import valores
n = float(input('Digite um numero: '))
a = float(input('Digite o acrescimo: '))
r = float(input('Digite o decrescimo: '))
print(f'O aumento de {n} em {a}% é: {valores.aumentar(n, a)}')
print(f'A redução do valor {n} em {r}% é: {valores.diminuir(n, r)}')
print(f'O dobro de {n} é {valores.dobro(n)}')
print(f'A metade de {n} é {valores.metade(n)}')
