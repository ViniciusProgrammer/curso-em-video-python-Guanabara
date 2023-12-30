print('Valores ímpares e múltiplos de 3 entre 1 e 500')

soma_valores = 0
quantidade = 0
for i in range(1, 501, 2):
    if i  % 3 == 0:
        quantidade += 1
        soma_valores += i
print('A soma entre os {} valores impares e multiplios por 3 é = {}'.format(quantidade, soma_valores))
