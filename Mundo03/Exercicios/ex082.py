valores = []
impares = []
pares = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('Todas as listas ordenadas em ordem crescente abaixo!')
valores.sort()
pares.sort()
impares.sort()
print(f'A lista completa: {valores}')
print(f'A lista de pares: {pares}')
print(f'A lista de impares: {impares}')
