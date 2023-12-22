velocidade = float(input('Informe a velocidade do carro: '))

if(velocidade > 80):
    multa = velocidade - 80
    print('Opa, você foi multado, e a sua multa irá custar R${:.2f}'.format(multa * 7))
else:
    print('Bom dia!, ótima dirigibilidade, continue assim!')
