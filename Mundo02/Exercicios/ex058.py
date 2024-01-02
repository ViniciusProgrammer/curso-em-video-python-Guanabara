from random import randint
from time import sleep

print('Irei pensan em um valor entre 0 e 10. Tente advinhar...')
print('Pensando...')
sleep(2)

tentativas = 0
computador = randint(0, 10)
jogador = int(input('Digite um valor entre 0 e 10: '))
tentativas += 1

if jogador < computador:
    print('Mais, eu pensei no valor {} e você no valor {}'.format(computador, jogador))
else:
    print('Menos, eu pensei no valor {} e você no valor {}'.format(computador, jogador))

while jogador != computador:
    print('\n')
    print('Você errou, tente novamente!')
    print('Pensando novamente...')
    sleep(2)
    computador = randint(0, 10)
    jogador = int(input('Digite um valor entre 0 e 10: '))
    if jogador < computador:
        print('Mais, eu pensei no valor {} e você no valor {}'.format(computador, jogador))
        tentativas += 1
    else:
        print('Menos, eu pensei no valor {} e você no valor {}'.format(computador, jogador))
        tentativas += 1
    print('Processando...')
    sleep(2)
    print('Eu pensei no valor {} e você no valor {}'.format(computador, jogador))

if jogador == computador:
    print('Parabéns, você acertou!')
    print('Pensamos no mesmo valor {}'.format(computador))
    print('Você precisou de {} tentativas para acertar, Parabens!'.format(tentativas))
