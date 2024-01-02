num = int(input('Informe um valor e veja o seu fatorial: '))
fatorial = 1

while num > 0:
    fatorial *= num
    num -= 1
print('O fatorial é {}'.format(fatorial))
