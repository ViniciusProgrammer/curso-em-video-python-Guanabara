from datetime import date

sexo = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0] 
if sexo == 'M':
    nascimento = int(input('Informe o seu ano de nascimento: '))
    idade = date.today().year - nascimento #quantidade de anos que pessoa tem
    idade_certa = 18
    print('Você nasceu em {}, você possui {} anos de idade\n'.format(nascimento, idade))

    if idade < idade_certa:
        print('Ainda faltam {} anos para o seu alistamento'.format(idade_certa - idade))
        print('O ano do seu alistamento será em {}'.format(date.today().year + (idade_certa - idade)))
    elif idade > idade_certa:
        print('Você tem {} anos, então já deveria ter se alistado!'.format(date.today().year - nascimento))
        print('Você deveria ter se alistado no ano de {}'.format((date.today().year) - (idade - idade_certa)))
    else:
        print('Você tem {} anos, chegou o momento de se alistar!'.format(date.today().year - nascimento))
else:
    print('Você não precisa se alistar!')
