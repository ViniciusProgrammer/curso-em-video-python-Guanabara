while True:
    num = int(input('Informe um número e veja a sua tabuada: '))
    if num >= 0:
        print('-' * 20)
        cont = 1
        while cont <= 10:
            print(f'{num} x {cont} = {num * cont}')
            cont += 1
        print('-' * 20)
    else:
        break
print('Programa da tabuada encerrado, volte sempre!')
