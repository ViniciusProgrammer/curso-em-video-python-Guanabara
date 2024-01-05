lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3:])
print(lanche[:-1])
print(lanche[-1])
print(lanche[::-1]) # Mostra a tupla inteira ao contrario

#Sem precisar informar a posição, podemos usar o for para mostrar todos os elementos da tupla
for i in lanche:
    print(f'{i}', end=' ')
print('\n')

'''Outra forma de fazer o for já indexados

for i in range(0, len(lanche)):
    print(f'Na posição {i} = {lanche[i]}')
print('\n')

Utilizando o enumerate

for pos, comida in enumerate(lanche):
    print(f'Na posição {pos} = {comida}')
print('\n')
'''

#Podemos usar o sorted para mostrar a tupla em ordem alfabetica, lembrando que sorted não altera a tupla, apenas mostra ela em ordem alfabetica
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Podemos junta-las
print(c)
print(len(c))
print(c.count(5)) # Mostra quantas vezes aparece o numero 5 na tupla
print(c.index(8)) # Mostra em que posição está o numero 8 na tupla
print(c.index(5, 1)) # Mostra em que posição está o numero 5 na tupla, começando a procurar a partir da posição 1
print(c.index(2, 4)) # Mostra em que posição está o numero 2 na tupla, começando a procurar a partir da posição 4

#As tuplas podemos declarar com elementos que não somos do mesmo tipo, como por exemplo:
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

#Podemos apagar uma tupla inteira, mas não podemos apagar apenas um elemento da tupla
del(pessoa)
