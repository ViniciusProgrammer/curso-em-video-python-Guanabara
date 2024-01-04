from random import randint
print('=-' * 23)
print('\tVAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 23)
cont = 0

while True:
    soma = 0
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = computador + jogador
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    print(f'A soma foi {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if soma % 2 == 0:
        resultado = 'P'
        if resultado == escolha:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        resultado = 'I'
        if resultado == escolha:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!, você venceu {cont} vezes.')
