numeros = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezez')
if 3 in numeros:
    print(f'O valor 3 está na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
print('\n')
