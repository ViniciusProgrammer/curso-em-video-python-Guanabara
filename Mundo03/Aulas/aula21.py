#Docstrings
'''
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
help(contador)

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
somar() #posso passar 0 argumentos, e o python vai atribuir 0 aos parametros padrão

#Escopo de variáveis

def teste():
    x = 8 #variavel local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
#programa principal
n = 2 #variavel global
print(f'No programa principal, n vale {n}')
teste()
'''

#Retorno de valores
def somar(n1, n2):
    soma = n1 + n2
    return soma

soma_valores = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
somar(num1, num2)
soma_valores = somar(num1, num2)
print(f'A soma dos valores é {soma_valores}')
