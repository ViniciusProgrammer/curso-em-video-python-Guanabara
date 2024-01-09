pessoas = {'nome': 'Vinicius', 'sexo': 'M',  'idade': 25}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('Usando o for com o keys')
for k in pessoas.keys():
    print(k, end=' ')
print()

print('Usando o for com o values')
for k in pessoas.values():
    print(k , end=' ')
print()

print('Usando o for com o items')
for k, v in pessoas.items():
    print(f'{k} = {v}', end=' ')
print()

print('Deletando um item do dicionário')
del pessoas['sexo']
print(pessoas)

print('Alterando um item do dicionário')
pessoas['nome'] = 'Leandro'
print(pessoas['nome'])

print('Adicionando um item no dicionário')
pessoas['peso'] = 56.5
print(pessoas)

print('Dict dentro de listas')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
esrado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(esrado2)
print(brasil)
print(brasil[0])
print(brasil[1])

print('Acessando um item do dicionário dentro de uma lista')
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print('Lendo dados para um dicionario e colocando em uma lista')
estado = {}
brasil = []

for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for i in brasil:
    for k, v in i.items():
        print(f'O campo {k} tem valor {v}')
    print()
