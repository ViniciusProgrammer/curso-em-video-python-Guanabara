from time import sleep
from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[c]} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')
valores = []
sorteia(valores)
somaPar(valores)
