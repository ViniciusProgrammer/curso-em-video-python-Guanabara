num = int(input('Informe um valor e veja seu fatorial: '))
fatorial = 1

for i in range(num, 0, -1):
    fatorial *= i
print('O fatorial de {} é igual a {}'.format(num, fatorial))
