casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
meses = anos * 12

prestacao = casa / meses
condicao = salario * (30 / 100)

if prestacao > condicao:
    print('Empréstimo NEGADO!')
    print('Devido a sua renda, o valor da prestação excede 30% do seu salário.')
    print('O valor da prestação seria de R${:.2f} por {} meses.'.format(prestacao, meses))
else:
    print('Empréstimo APROVADO!')
    print('Suas parcelas serão de R${:.2f} por {} meses.'.format(prestacao, meses))
