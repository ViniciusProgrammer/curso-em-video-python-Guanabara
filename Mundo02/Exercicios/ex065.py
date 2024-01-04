media = maior = menor = quantidade = 0
condicao = True
i = 1

while condicao != False:
    num = int(input('Informe um valor: '))
    media += num
    quantidade += 1

    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    i += 1
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        condicao = False
    else:
        condicao = True
print('A média dos {} valores digitados é = {:.2f}'.format(quantidade, media / quantidade))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
