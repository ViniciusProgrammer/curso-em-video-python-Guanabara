'''
Modularização:

    - Dividir um programa grande em vários arquivos pequenos
    - Facilita a manutenção
    - Cada arquivo é chamado de módulo
    - Módulos podem ser chamados de outros módulos
    
Exemplo:

def fatorial(num):
    f = 1
    for c in range(1, num+1):
        f *= c
    return f
num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

'''