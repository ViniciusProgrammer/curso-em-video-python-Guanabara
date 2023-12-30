soma_pares = 0
quantidade = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if numero % 2 == 0:
        quantidade += 1
        soma_pares += numero
print('A soma dos {} números pares digitados é = {}'.format(quantidade, soma_pares))
