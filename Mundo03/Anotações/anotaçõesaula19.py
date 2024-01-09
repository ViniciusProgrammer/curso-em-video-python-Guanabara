'''
Dicionários em Python
Declaração:
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}

Printando
print(dados['nome']) # Pedro
print(dados['idade']) # 25

Para adicionar um novo elemento:

dados['sexo'] = 'M'

a estrutura fica assim:
dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
                   nome           idade        sexo             essa parte de baixo é chmao de chave(keys)
para remover um elemento:

del dados['idade'] por exemplo

Exemplo:

filme = { 'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas' }

a estrutura fica assim:
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

print(filme.values()) # Esse comando ira printar os elementos ['Star Wars', 1977, 'George Lucas']

print(filme.keys()) # Esse comando ira printar as chaves ['titulo', 'ano', 'diretor']

Para pegar o valor e a chave ao mesmo tempo:

print(filme.items()) # Esse comando ira printar os elementos e as chaves [('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')]


Pode-se fazer um for para printar os elementos e as chaves:

for k, v in filme.items():
    print(f'O {k} é {v}')

    
Pode-se criar uma lista com dicionários dentro:

locadora = []

filme1 = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
filme2 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
filme3 = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}

locadora = [filme1, filme2, filme3]

print(locadora[0]['ano']) # 1977
print(locadora[2]['titulo']) # Matrix
print(locadora[1]['diretor']) # Joss Whedon


'''