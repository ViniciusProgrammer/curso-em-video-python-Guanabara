#Trabalhando com módulos

'''
Exemplos de importação de módulos em Python
Quando eu querer importar um módulo inteiro eu uso o seguinte comando:
import math = recebe todas as funções do módulo math

Quando eu quiser importar apenas uma função específica de um módulo eu uso o seguinte comando:
from math import sqrt = importa apenas a função sqrt do módulo math
Dessa forma não é preciso usar o nome math antes da função sqrt pois só de colocar sqrt já é o suficiente

Algynas funções do módulo math:

a funcao ceil faz um arredondamento para cima
a funcao floor faz um arredondamento para baixo
a funcao trunc trunca o valor de um número ou seja ele elimina a parte fracionária de um número
a funcao pow faz a potenciação de um número
a funcao sqrt faz a raiz quadrada de um número
a funcao factorial faz o fatorial de um número

import random
num = random.random() = gera um número float aleatório entre 0 e 1
num = random.randint(1, 10) = gera um número inteiro aleatório entre 1 e 10 esses parametros podem ser alterados
print(num)

Dicas do exercicio 019:
Resolução do exercício 019 do curso de Python do canal Curso em Vídeo do professor Gustavo Guanabara

import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4] # Cria uma lista com os nomes dos alunos, lista no Python é dessa forma
escolhido = random.choice(lista) # Escolhe um item aleatório de uma lista
print('O aluno escolhido foi {}'.format(escolhido))

'''