f = str(input('Digite uma frase qualquer: ')).strip().upper()
palavra = f.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A palavra é um palindromo')
else:
    print('A palavra NÃO é')

'''inverso = junto[::-1]'''
