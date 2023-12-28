from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)

print('Vamos jogar Jokenpô?')
print('Escolha e escreva a sua jogada [Pedra, Papel ou Tesoura]')

jogador = str(input('Qual a sua jogada? ')).strip().capitalize()

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == jogador:
    print('Empate!')
    print('Pensamos iguais!')
elif computador == 'Pedra' and jogador == 'Papel':
    print('Você ganhou!')
    print('Eu pensei em {} e você em {}.'.format(computador, jogador))
elif computador == 'Pedra' and jogador == 'Tesoura':
    print('Você perdeu!')
    print('Eu pensei em {} e você em {}.'.format(computador, jogador))
elif computador == 'Papel' and jogador == 'Pedra':
    print('Você perdeu!')
    print('Eu pensei em {} e você em {}.'.format(computador, jogador))
elif computador == 'Papel' and jogador == 'Tesoura':
    print('Você ganhou!')
    print('Eu pensei em {} e você em {}.'.format(computador, jogador))
elif computador == 'Tesoura' and jogador == 'Papel':
    print('Você perdeu!')
    print('Eu pensei em {} e você em {}.'.format(computador, jogador))
elif computador == 'Tesoura' and jogador == 'Pedra':
    print('Você ganhou!')
    print('Eu pensei em {} e você em {}.'.format(computador, jogador))
else:
    print('Escolha inválida!')
