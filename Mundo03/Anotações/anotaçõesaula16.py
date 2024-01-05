'''
Variaveis Compostas - Tuplas

#TUPLAS SÃO IMUTAVEIS

São variaveis que guardam mais de um valor, como uma lista, mas são imutaveis, ou seja, não podem ser alteradas.

Exemplo 1:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche) se printar dessa forma irá aparecer todos os elementos da tupla
print(lanche[0:2]) se for dessa forma irá aparecer apenas os elementos de 0 a 2, ou seja, Hamburguer e Suco
assim como no fatiamento de strings, o ultimo elemento não é mostrado, ou seja, o elemento 2 não aparece

print(lanche[1:]) irá aparecer todos os elementos a partir do elemento 1, ou seja, Suco, Pizza e Pudim
print(lanche[-1]) irá aparecer o ultimo elemento, ou seja, Pudim
print(lanche[-2]) irá aparecer o penultimo elemento, ou seja, Pizza
print(lanche[-3:]) irá aparecer os 3 ultimos elementos, ou seja, Suco, Pizza e Pudim
print(lanche[-4:]) irá aparecer todos os elementos, ou seja, Hamburguer, Suco, Pizza e Pudim

Podemos usar a fubção len() para saber quantos elementos tem na tupla
'''