def mostralinha():
    print('-'*50)
mostralinha()
print('AULA 20'.center(50))
mostralinha()

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
year = int(input('ANO: '))
print(is_leap(year))
def mensagem(msg):
    print('-' * 50)
    print(f'{msg}'.center(50))
    print('-' * 50)
msg = str(input('=>'))
mensagem(msg)
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A+B é igual a {s}')
soma(b=4, a=5)

def contador(* num):
    for v in num:
        dobra = v * 2
        print(dobra, end=' ')
    total = sum(num)
    print(f'Somando os numeros {num} A soma é {total}')
    print('FIM')
contador(2, 8)
contador(7, 1, 9)
contador(5, 3, 9, 1, 6)

valores= [6, 3, 9, 1, 0, 2]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos += 1
dobra(valores)
print(valores)
