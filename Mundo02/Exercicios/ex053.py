frase = str(input('Informe uma frase: ')).strip().upper()

inversa = frase[::-1]

print('O inverso de {} é {}'.format(frase, inversa))

if frase == inversa:
    print('A frase é um PALINDROMO!')
else:
    print('A frase não é um PALINDROMO')
