print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
aux = razao

while aux < (razao * 11):
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
    aux += razao
print('FIM')

'''
Outra forma de fazer:
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 1
termo = primeiro_termo

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

'''