dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)
pessoas = list()
pessoas.append(dados[:]) #uma lista dentro de outra
print(pessoas)
print(pessoas[0][0])
galera = [['Joao', 20],['Maria', 22],['Pedro', 19]]
print(galera[0])
for p in galera:
    print(p[0])
    