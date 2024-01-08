matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = terceira_coluna = maior_valor = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a linha {i} e coluna {j}: '))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            terceira_coluna += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
print('Segue abaixo a matriz 3 x 3')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor}')

# Resolução do professor Guanabara:
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# soma_pares = terceira_coluna = maior_valor = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         matriz[i][j] = int(input(f'Digite um valor para a linha {i} e coluna {j}: '))
# print('Segue abaixo a matriz 3 x 3')
# for i in range(0, 3):
#     for j in range(0, 3):
#         print(f'[{matriz[i][j]:^5}]', end='')
#         if matriz[i][j] % 2 == 0:
#             soma_pares += matriz[i][j]
#     print()
# print(f'A soma dos valores pares é {soma_pares}')
# for i in range(0, 3):
#     terceira_coluna += matriz[i][2]
# print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
# for j in range(0, 3):
#     if j == 0:
#         maior_valor = matriz[1][j]
#     elif matriz[1][j] > maior_valor:
#         maior_valor = matriz[1][j]
# print(f'O maior valor da segunda linha é {maior_valor}')
