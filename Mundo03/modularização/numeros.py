import funcoes
num = int(input('Digite um valor: '))
fat = funcoes.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {funcoes.dobro(num)}')
print(f'O triplo de {num} é {funcoes.triplo(num)}')
