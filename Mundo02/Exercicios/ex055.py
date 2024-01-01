menor_peso = 0.0
maior_peso = 0.0

for i in range(1, 6):
    peso = float(input('Informe a sua massa corporal em (Kg): '))
    if i == 1:
        maior_peso = menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso
print('O maior peso lido foi de {}Kg'.format(maior_peso))
print('O menor peso lido foi de {}Kg'.format(menor_peso))
