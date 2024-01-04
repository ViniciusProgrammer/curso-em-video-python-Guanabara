from time import sleep
dezoito = homens = vinte_anos = 0

while True:
    print('=-' * 21)
    print('\tCADASTRE UMA PESSOA')
    print('=-' * 21)

    idade  = 0
    while idade <= 0:
        idade = int(input('Informe a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        vinte_anos += 1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'S':
        print('Ok, vamos continuar...')
        continue
    else:
        break
print('Finalizando...')
sleep(2)
print(f'Foram cadastradas {dezoito} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')

if vinte_anos == 0:
    print('Não foram cadastradas mulheres com menos de 20 anos.')
elif vinte_anos == 1:
    print('Foi cadastrada 1 mulher com menos de 20 anos.')
else:
    print(f'Foram cadastradas {vinte_anos} mulheres com menos de 20 anos.')
