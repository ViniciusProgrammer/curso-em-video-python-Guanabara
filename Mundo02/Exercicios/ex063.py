print('-=-=' * 11)
print('\tSEQUÊNCIA DE FIBONACCI')
print('-=-=' * 11)
n_termos = int(input('Informe a quantidade de termos que você deseja ver: '))
termo1= 0
termo2 = 1

print('~' * 30)
print('{} -> {}'.format(termo1, termo2), end='')

i = 3
while i <= n_termos:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    termo1 = termo2 
    termo2 = termo3  
    i += 1
print(' -> FIM!')
print('~' * 30)
