from time import sleep
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

print('=-' * 16)
print('\tMenu de opções')
print('=-' * 16, end='')

print('''      
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] VERIFICAR O MAIOR VALOR
[ 4 ] INFROMAR NOVOS VALORES
[ 5 ] SAIR DO PROGRAMA''')
print('=-' * 16)

escolha = False

while not escolha:
    print('\n')
    opcao = int(input('>>>>>>>>>>>  Selecione a sua escolha: '))
    if opcao == 1:
        print('A soma entre {} e {} é = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('Entre {} e {} o MAIOR é {}'.format(num1, num2, num1))
        elif num1 < num2:
            print('Entre {} e {} o MAIOR é {}'.format(num2, num1, num2))
        else:
            print('Os {} e {} são iguais!'.format(num1, num2))
    elif opcao == 4:
        print('Informe os novos valores!')
        num1 = int(input('Informe o novo primeiro número: '))
        num2 = int(input('Informe o novo segundo número: '))
    elif opcao < 1 or opcao > 5:
        print('Opção inválida, tente novamente!')
    else:
        escolha = True
        print('Finalizando...')
        sleep(2)
        print('Programa finalizado com sucesso!')
