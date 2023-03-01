n = int(input("Verificar numeros primos ate: "))
contador = 0
for c in range(2, n):
    if (n % c == 0):
        print("Múltiplo de", c)
        contador += 1

if contador == 0:
    print("É primo")
else:
    print("Tem", contador, " múltiplos acima de 2 e abaixo de", n)
