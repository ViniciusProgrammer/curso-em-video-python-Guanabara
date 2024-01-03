i = quantidade = soma_total = 0
while i != 999:
    num = int(input('Digite um valor ou [999] para parar: '))
    if num != 999:
        soma_total += num
        quantidade += 1
    else:
        i = num
print('A soma dos {} valores digitados é = {}'.format(quantidade, soma_total))
