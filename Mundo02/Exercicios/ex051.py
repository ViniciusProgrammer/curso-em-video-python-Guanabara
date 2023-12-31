print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

for i in range(primeiro_termo, primeiro_termo + razao * 10, razao):
    print(i, end=' -> ')
print('FIM')
