primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
condicao = 1

for i in range(primeiro_termo, primeiro_termo + razao * 10, razao):
    print(i, end=' -> ')
print('PAUSA')
while condicao != 0:
    quantidade = int(input('Quantos termo a mais vc quer ver? '))
    if quantidade == 0:
        condicao = 0
    else:
        for i in range(primeiro_termo + razao * 10, primeiro_termo + razao * (10 + quantidade), razao):
            print(i, end=' -> ')
        print('PAUSA')
        condicao = int(input('Digite 0 se quiser encerrar, ou qualquer outro número para continuar: '))
print('FIM')
