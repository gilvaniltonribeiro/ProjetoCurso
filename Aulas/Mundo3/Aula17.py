lista = ['cafe', 'leite', 'acucar', 'ovo', 'carne']
lista.append('agua') #adiciona um valor a variavel
print(lista)
del lista[0] #remove pelo indice direto
lista.pop() #remove o ultimo da lista mas pode alterar no indice
lista.remove('leite') #remove pelo conteudo
valores = list(range(5, 15))
valores.sort(reverse=True)
valores.insert(0, 100) #adiciona um valor na posicao q vc quiser
print(valores)
print(f'Essa lista tem {len(valores)} valores')
for c, v in enumerate(valores):
    print(f'Na posicao {c} tal encontrei tal {v}...')
new_list = list()
for c in range(0, 5):
    new_list.append(int(input('Digite um valor: ')))
print(f'Voce digitou {new_list}')
b = new_list[:] #criando uma copia de lista
