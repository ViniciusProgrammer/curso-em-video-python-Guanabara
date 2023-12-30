numero = int(input('Informe um valor e veja a sua tabuada: '))
print('-=' * 6)
for i in range(1, 11):
    print('{} x {:>2} = {:>2}'.format(numero, i, numero * i))
print('-=' * 6)
