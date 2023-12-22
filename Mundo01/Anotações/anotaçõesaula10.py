'''
No python tempos 3 tipos de condições:
Mas nessa aula utilizaremos apenas duas delas:
1 - Condição Simples
Se baseia em apenas uma condição de anákise
que no caso é o comando if

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')

2 - Condição Composta
Se baseia em duas condições de análise
que no caso são os comandos if e else

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

existe também uma opcao de simplificada

tempo = int(input('Quantos anos tem seu carro? '))

print('Carro novo' if tempo <= 3 else 'Carro velho')
dessa maneira em uma linha só

O python nao possui operador ternário


'''