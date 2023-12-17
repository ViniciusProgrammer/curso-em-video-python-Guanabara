carteira = float(input('Quanto em R$ você possui na carteira? R$: '))
dolar = 3.27
print('Com R${:.2f} você pode adquirir U${:.2f} dólares'.format(carteira, carteira/dolar))
