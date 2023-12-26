numero = int(input('Informe um número: '))
print('\n[1] para binário\n[2] para octal\n[3] para hexadecimal\n')

escolha = int(input('Escolha uma das opções acima: '))

if escolha == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')
