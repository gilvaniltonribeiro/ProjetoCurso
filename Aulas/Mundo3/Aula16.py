#TUPLAS e variaves compostas
#() = Tuplas
#[] = Listas
#{} = dicionario
lanche = ('pizza', 'suco', 'hambur')
for c in range(0, len(lanche)):
    print(f'Comi {lanche[c]}')
#for comida in lanche:
    #print(f'Vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posicao {pos}')
teste = (1, 2, 3, 4, 245, 29, 9, 72, 8)
print(teste.count(2)) #contar
print(teste.index(1)) #ver a posição
