print('Nuḿeros pares que estão entre 1 e 50')
print("{", end='')
for i in range(1, 51):
    if i % 2 == 0 and i != 50:
        print(i, end=', ')
    else:
        if i == 50 and i % 2 == 0:
            print(i, end='')
print('} FIM!')

#Outra forma de fazer
'''
for j in range(2, 51, 2):
   print(j, end= ' ')
print('Acabou!')
'''
