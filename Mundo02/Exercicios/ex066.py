quantidade = soma = 0

while True:
    num = int(input('Digite um valor ou [999 para PARAR!]: '))
    if num == 999:
        break
    else:
        soma+= num
        quantidade += 1
print(f'A soma dos {quantidade} valores digitados é {soma}')
