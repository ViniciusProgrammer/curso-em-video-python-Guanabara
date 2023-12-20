numero = int(input("Digite um valor entre 0 e 9999: "))

milhar = numero // 1000
centena = numero % 1000 // 100
dezena = numero % 100 // 10
unidade = numero % 10

print('Analisando o número {}... '.format(numero))
print('Unidade = {}'.format(unidade))
print('Dezena = {}'.format(dezena))
print('Centena = {}'.format(centena))
print('Milhar = {}'.format(milhar))
