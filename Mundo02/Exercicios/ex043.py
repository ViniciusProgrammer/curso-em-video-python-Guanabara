peso = float(input('Informe a sua massa corporal: (Kg) '))
altura = float(input('Informe a sua altura: (m) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('O seu IMC é {:.1f}'.format(imc))
    print('Você está abaixo do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é {:.1f}'.format(imc))
    print('O seu peso está IDEAL')
elif imc >= 25 and imc < 30:
    print('O seu IMC é {:.1f}'.format(imc))
    print('Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('O seu IMC é {:.1f}'.format(imc))
    print('Você está com OBESIDADE')
else:
    print('O seu IMC é {:.1f}'.format(imc))
    print('Você está com OBESIDADE MÓRBIDA')
