from arquivo import *

def imprimiTexto(msg):
    print('-' * 50)
    print('{: ^50}'.format(msg))
    print('-' * 50)


def exibeMenu():
    imprimiTexto('MENU PRINCIPAL')
    print('\033[1;33m1 - Ver pessoas cadastradas\033[m')
    print('\033[1;33m2 - Cadastrar nova pessoa\033[m')
    print('\033[1;33m3 - Sair do Sistema\033[m')
    print('-' * 50)


def verificaOpcao(msg):
    try:
        op = int(input(msg))
    except:
        print('\033[1;31mOpção Inválida! Digite Novamente...\033[m')
        return verificaOpcao(msg)
    
    if op > 0 and op < 4:
        return op
    else:
        print('\033[1;31mOpção Inválida! Digite Novamente...\033[m')
        return verificaOpcao(msg)


def leiaIdade(msg):
    while True:
        n = input(msg)

        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite uma idade válida')
    