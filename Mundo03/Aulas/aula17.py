numeros = [2, 5, 9, 12]
print(f'Valores na lista = {numeros}')
numeros.append(19)
print(f'Lista alterada = {numeros}')
numeros.sort()
print(f'Lista ordenada crescente = {numeros}')
numeros.sort(reverse=True)
print(f'Lista ordenada de forma decrescente = {numeros}')
print(f'Essa lista tem {len(numeros)} elementos')
print('Irei adicionar o valor 0 na posição 2 da lista na proxima linha')
numeros.insert(2, 0) # passa a posição e o valor nessa ordem para funcionar
print(f'Lista alterada = {numeros}')
print('Essa lista tem {} elementos'.format(len(numeros)))
numeros.pop()
print(f'Lista alterada = {numeros}')
print('Essa lista tem {} elementos'.format(len(numeros)))
numeros.pop(2)
print(f'Lista alterada = {numeros}')
print('Essa lista tem {} elementos'.format(len(numeros)))

numeros.append(2)
numeros.append(5)
numeros.append(2)
print(f'Lista alterada = {numeros}')

for i in numeros:
    if 2 in numeros:
        numeros.remove(2)
    else:
        print('Não tem o número 2 na lista')
        break
print(f'Lista alterada = {numeros}')

valores = []
for i in range(0, 5):
    num = int(input('Informe um valor: '))
    valores.append(num)
print('Valores adicionados com sucesso!')
print(f'A lista contém os valores = {valores}')
print('\n')

for pos, i in enumerate(valores):
    print(f'Na posição {pos + 1} encontrei o valor {i}')
print('Cheguei ao final da lista')

print('\nLigações entre listas')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\nCópia de listas')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
