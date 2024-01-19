'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função chamada leiaFloat com a
mesma funcionalidade.
'''

def leiaInt(msg):
    try:
        n = str(input(msg))
        if n == '':
            print('\033[1;31mO usuário preferiu não digitar\033[m')
            return 0
        n = int(n)
    except:
        print('\033[1;31mERRO! Digite um número Inteiro válido\033[m')
        return leiaInt(msg)
    else:
        return n
    

def leiaFloat(msg):
    try:
        n = str(input(msg))
        if n == '':
            print('\033[1;31mO usuário preferiu não digitar\033[m')
            return 0
        n = float(n)
    except:
        print('\033[1;31mERRO! Digite um número Real válido\033[m')
        return leiaFloat(msg)
    else:
        return n


numeroInt = leiaInt('Digite um número Inteiro: ')
numeroFloat = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {numeroInt}, já o real foi {numeroFloat}.')
