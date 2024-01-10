'''
def linha():
    print('-' * 26)

linha()
print('   CURSO EM VÍDEO   ')
linha()
linha()
print('   APRENDA PYTHON   ')
linha()
linha()
print('   GUSTAVO GUANABARA   ')
linha()

def mensagem(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))
for i in range(0, 3):
    txt = str(input('Insira uma mensagem: '))
    mensagem(txt)
    if i == 2:
        print('Acabou!')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma entre A + B = {a + b}')
num1 = int(input('Digite um valor para A: '))
num2 = int(input('Digite um valor para B: '))
soma(num1, num2)

def dobra_valores(lista):
    for i in lista:
        print(f'{i * 2}', end=' ')

valores = [2, 5, 9, 1]
dobra_valores(valores)
print()
'''

def dobra_valores(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
valores = [2, 5, 9, 1]
dobra_valores(valores)
print(valores)
