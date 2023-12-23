salario = float((input('Informe o seu salário: R$')))

if salario <= 1250.00:
    aumento = salario + (salario * (15/100))
    print('O seu salário passará a ser R${:.2f} com o aumento de 15%'.format(aumento))
else:
    aumento = salario + (salario * 10/100)
    print('O seu salário passará a ser R${:.2f} com o aumento de 10%'.format(aumento))
