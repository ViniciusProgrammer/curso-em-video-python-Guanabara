from time import sleep
print('=-' * 21)
print('\tLOJA SUPER BARATÃO')
print('=-' * 21)

valor_do_mais_barato = 0
acimade1000 = 0
mais_barato = ''
total_compras = 0
i = 0
while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip().upper()
    valor_produto = float(int(input('Informe o valor do produto: R$ ')))
    if i == 0:
        mais_barato = nome_produto
        valor_do_mais_barato = valor_produto
        if valor_produto > 1000:
            acimade1000 += 1
            total_compras += valor_produto
        else:
            total_compras += valor_produto
    else:
        if valor_produto < valor_do_mais_barato:
            mais_barato = nome_produto
            valor_do_mais_barato = valor_produto
            total_compras += valor_produto
            acimade1000 += 1
        else:
            if valor_produto > 1000:
                acimade1000 += 1
                total_compras += valor_produto
            else:
                total_compras += valor_produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'S':
        print('Ok, vamos continuar...')
    else:
        break
    i += 1
print('Finalizando...')
sleep(2)
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto na compra foi de R$ {total_compras:.2f}.')
print(f'{acimade1000} produtos custam mais de R$ 1000,00.')
print(f'O produto mais barato é {mais_barato} e custa R$ {valor_do_mais_barato:.2f}.')
