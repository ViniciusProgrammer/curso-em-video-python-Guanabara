valores = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    valores.append(num)
for i in range(len(valores)):
    troca = False
    for j in range (len(valores) -i -1):
        if valores[j] > valores[j + 1]:
            valores[j], valores[j + 1] = valores[j + 1], valores[j]
            troca = True
    if not troca:
        break
print(valores)

# Solução do Guanabara
'''valores = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(valores)
'''
