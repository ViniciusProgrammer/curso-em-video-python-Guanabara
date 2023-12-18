import math
num = int(input('Informe um valor: '))
raiz = math.sqrt(num)
print('A raiz de {} é = {}'.format(num, raiz))
#Dessa forma acima o arredondamento não está presente
print('A raiz de {} é = {}'.format(num, math.ceil(raiz)))
#Dessa forma acima o arredondamento está presente
