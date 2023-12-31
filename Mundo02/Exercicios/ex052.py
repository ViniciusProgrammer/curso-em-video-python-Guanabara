numero = int(input('Informe um valor: '))
qtd_divisores = 0

for i  in range(1, numero + 1):
    if numero % i == 0:
        print('\033[31m', end='')
        qtd_divisores += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi dividido por {} vezes'.format(numero, qtd_divisores))

if qtd_divisores  == 2:
    print('O número {} é PRIMO!'.format(numero))
else:
    print('O número {} NÃO É PRIMO!'.format(numero))
