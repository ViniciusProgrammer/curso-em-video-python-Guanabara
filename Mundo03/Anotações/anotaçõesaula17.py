'''
Variaveis Compostas (Listas) - Aula 17

Tuplas são imutáveis
Listas são mutáveis
Essas são as principais diferenças entre elas

Lista é uma variável composta que permite armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
Podemos ter listas com tipos de dados diferentes
As listas são mutáveis, ou seja, podemos alterar o conteúdo de uma lista e adiconar ou remover elementos
As listas são representadas por colchetes: []

Para adicionar elementos em uma lista, usamos o comando append()
Exemplo de lista:
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche.append('cookie') isso faz com que o elemento 'cookie' seja adicionado ao final da lista na posição 4 dessa lista

Para adicionar elementos em uma lista, usamos o comando insert()
esse comando podemos adiconar em qualquer posição da lista é só colocar o número da posição que queremos adicionar o elemento

Exemplo:
lanche.insert(0, 'cachorro quente') isso faz com que o elemento 'cachorro quente' seja adicionado na posição 0 da lista
Mas se quiser adicionar na posição 2, é só colocar o número 2 no lugar do 0

Para remover elementos de uma lista temos 3 comandos:

del lanche[3] - deleta o elemento da posição 3 da lista
lanche.pop(3) - deleta o elemento da posição 3 da lista
*Normalmente usamos o pop() para remover o último elemento da lista, pois 
como padrão ele remove o último elemento da lsita
mas se quiser remover um elemento de uma posição específica, é só colocar o número da posição no parênteses

lanche.remove('pizza') - deleta o elemento 'pizza' da lista

Se quiser remover um elemento que não sabe a posição, mas sabe o nome do elemento, é só colocar o nome do elemento no parênteses

Exemplo:
if 'pizza' in lanche:
    lanche.remove('pizza')
else:
    print('Não tem pizza na lista')

Para criar uma lista atraves de um range, usamos o comando range()

Exemplo:

valores = list(range(4, 11)) - cria uma lista com os valores de 4 até 10

Outro exemplo:

valores = [8, 2, 5, 4, 9, 3, 0] Percerba que os valores estão fora de ordem

para ordenar os valores em ordem crescente, usamos o comando valores.sort()

Exemplo:

valores.sort() - ordena os valores em ordem crescente

para ordenar os valores em ordem decrescente, usamos o comando valores.sort(reverse=True)

Exemplo:

valores.sort(reverse=True) - ordena os valores em ordem decrescente

Uma forma de adicionar elementos numa lista através de um for é:

valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

Outra forma de adicionar elementos numa lista através de um for é:

valores = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    valoes.append(num)
print(valores)
print(f'Lista A: {a}')

a = [2, 3, 4, 7]
b = a
b[2] = 8 Ao fazer isso com a lista b ela mexe diretamente com a lista a pois essa forma de '=' cria uma ligaçao entre as duas listas
print(f'Lista B: {b}')

Para criar uma copia de lista devemos fazer da seguinte forma:

b = a[:] b recebe todos os elementos de a mas não cria uma ligação entre as duas listas

'''