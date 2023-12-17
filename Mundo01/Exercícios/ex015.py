dias = int(input('Informe a quantidade de dias que passou com o carro: '))
km = float(input('Informe a quantidade de quilometros percorridos: '))
pagamento = (dias * 60) + (km * 0.15)
print('O valor a ser pago pelo cliente corressponde ao valor R${:.2f}'.format(pagamento))
