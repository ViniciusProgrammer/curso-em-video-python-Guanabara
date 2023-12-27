from datetime import date
nascimento = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    print('Você tem {} anos e a sua categoria é MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e a sua categoria é INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e a sua categoria é JUNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e a sua categoria é SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e a sua categoria é MASTER'.format(idade))
