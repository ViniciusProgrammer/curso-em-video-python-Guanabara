'''
AULA 18 - LISTAS (PARTE 2)

Trabalhando com listas compostas

Exemplos:
dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)

Declarando de uma vez só  uma lista dentro de outra lista

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]

Programa que le dados e copia para outra lista e mostra somente os maiores de 21 anos
galera = []
dados = []
for i in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) # [:] copia todos os elementos de dados
    dados.clear() # limpa a lista dados
for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade.')
    else:
        print(f'{i[0]} é menor de idade.')
'''
