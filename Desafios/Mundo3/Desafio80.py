lista = []
for c in range(0, 5):
    n = (int(input('Digite o valor')))
    if c == 0 or n > max(lista):
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
