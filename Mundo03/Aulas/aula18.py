teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste)
print('Una lista dentro de otra lista:')
print(galera)

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[2][1])

print('Printando tudo:')
for i in pessoas:
    print(i)
print('Printando o nome das pessoas:')
for i in pessoas:
    print(i[0])
print('Printando a idade das pessoas:')
for i in pessoas:
    print(i[1])
print('Printando o nome e a idade das pessoas:')
for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos de idade.')

dados = []
nome_idade = []

for i in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    nome_idade.append(dados[:])
    dados.clear()
print(nome_idade)
