from random import randint
from time import sleep
computador = randint(0, 5)

usuario = int(input('Informe um valor: '))

print('Processando...')
sleep(2)

if(usuario == computador):
    print('Parabéns você acertou!')
else:
    print('Você perdeu!')
    print('O número pensado pelo computador foi {}'.format(computador))
