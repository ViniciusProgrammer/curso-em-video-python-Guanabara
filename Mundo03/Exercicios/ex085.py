principal = []
impares = []
pares = []
for i in range(0, 7):
    principal.append(int(input('Digite um valor: ')))
for i in principal:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')

#solução do Guanabara:
# num = [[], []]
# valor = 0
# for i in range(1, 8):
#     valor = int(input(f'Digite o {i}º valor: '))
#     if valor % 2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)
# num[0].sort()
# num[1].sort()
# print(f'Os valores pares digitados foram: {num[0]}')
# print(f'Os valores ímpares digitados foram: {num[1]}')
