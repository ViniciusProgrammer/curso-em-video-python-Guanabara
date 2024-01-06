valores = []
maior = menor = 0
indice_maior = []
indice_menor = []
for i in range(0, 5):
    num = int(input('Digite um valor na posição {}: '.format(i)))
    valores.append(num)
for p, i in enumerate(valores):
    if p == 0:
        maior = menor = i
        indice_maior.append(p)
        indice_menor.append(p)
    else:
        if i > maior:
            maior = i
            indice_maior = [p]
        elif i < menor:
            menor = i
            indice_menor = [p]
        elif i == maior:
            indice_maior.append(p)
        elif i == menor:
            indice_menor.append(p)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições {indice_maior}')
print(f'O menor valor digitado foi {menor} nas posições {indice_menor}')
