'''
Interactive Help
comando help()
help(print) esse parametro pode ser qualquer coisa
help(input)

outra forma não necessarimente pode ser igual ao help()
print(input.__doc__) # mostra a documentação do comando

Docstrings

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
    
Parametros opcionais

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2,)
A fnção tem 3 parametros, mas só foram passados 3 argumentos, então o python vai atribuir 0 aos parametros que não foram passados

Escopo de variáveis

exemplo:

def teste(n):
    x = 8 #variavel local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
#programa principal
n = 2 #variavel global
print(f'No programa principal, n vale {n}')
teste()

Temos como fazer com que uma variavel local se torne global, usando o comando global

def teste(n):
    global n1
    n1 = 4
    print(f'Na função teste, n1 vale {n1}')
#programa principal
n1 = 2
teste()
print(f'No programa principal, n1 vale {n1}')

Retorno de valores

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')

Exercícios
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
    
'''
