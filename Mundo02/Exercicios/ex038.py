num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O primeiro valor digitado é o MAIOR')
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor digitado é o MAIOR')
    print('{} é maior que {}'.format(num2, num1))
else:
    print('Não existe valor maior, os dois são iguais')
