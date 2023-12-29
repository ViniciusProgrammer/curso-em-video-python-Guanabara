print('Agora vamos fazer um contador de 0 a 5')
for i in range(1, 6):
    print('oi')
print('FIM\n')

print('Agora vamos fazer um contador de 0 a 6')
for i in range(6, 0, -1):
    print(i)
print('FIM\n')

print('Agora vamos fazer um contador de 0 a 6, pulando de 2 em 2')
for i in range(0, 7, 2):
    print(i)
print('Fim\n')     
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

for i in range(inicio, fim + 1, passo):
    print(i)
print('Fim\n')
