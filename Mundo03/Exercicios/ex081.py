valores = []
quantidade = 0
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        quantidade += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Foram digitados {quantidade} valores!')
print('A lista na ordem decrescente: {}'.format(sorted(valores, reverse=True)))
if 5 not in valores:
    print('O valor 5 não está na lista!')
else:
    print('O valor 5 está na lista!')
