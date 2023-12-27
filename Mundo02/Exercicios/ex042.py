lado1 = float(input('Informe o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do tri6angulo: '))
lado3 = float(input('Informe o terceiro lado do tri6angulo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('Podemos formar um tri6angulo!')
    if lado1 == lado2 == lado3:
        print('Triângulo EQUILATERO!')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triângulo ISÓSCELES!')
    elif lado1 != lado2 != lado3 != lado1:
        print('Triângulo ESCALENO!')
else:
    print('Não podemos formar um triângulo!')
