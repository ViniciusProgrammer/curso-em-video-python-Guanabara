#exemplo 1
i = 1

while i < 10:
    print(i)
    i += 1
print('FIM!\n')
    
#exemplo 2
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!\n')

#exemplo 3
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
