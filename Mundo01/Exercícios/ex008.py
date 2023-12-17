metros = float(input('Informe uma quantidade em metros: '))
centimetros = metros * 100
decimetros = metros * 10
milimetros = metros * 1000
decametro = metros / 10
hectometro = metros / 100
quilometro = metros / 1000
print('A quantidade informada pelo usuário em metros foi {}'.format(metros))
print('E a sua representação em decimetros corresponde a {:.0f} decimetros'.format(decimetros))
print('E a sua representação em centimetros corrsponde a {:.0f} centimetros'.format(centimetros))
print('E a sua representação em milimetros corresponde a {:.0f} milimetros'.format(milimetros))
print('E a sua representação em decametros corresponde a {} decametros'.format(decametro))
print('E a sua representação em hectometros corresponde a {} hectometros'.format(hectometro))
print('E a sua representação em quilometros corresponde a {} quilometros'.format(quilometro))
