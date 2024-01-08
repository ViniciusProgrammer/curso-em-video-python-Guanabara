from time import sleep
from random import randint
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for c in range(0, quant):
    jogo = []
    for n in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

# Versão do Guanabara
#from random import randint
#from time import sleep
#lista = list()
#jogos = list()
#print('-' * 30)
#print(f'{"JOGA NA MEGA SENA":^30}')
#print('-' * 30)
#quant = int(input('Quantos jogos você quer que eu sorteie? '))
#tot = 1
#while tot <= quant:
#    cont = 0
#    while True:
#        num = randint(1, 60)
#        if num not in lista:
#            lista.append(num)
#            cont += 1
#        if cont >= 6:
#            break
#    lista.sort()
#    jogos.append(lista[:])
#    lista.clear()
#    tot += 1
#print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
#for i, l in enumerate(jogos):
#    print(f'Jogo {i + 1}: {l}')
#    sleep(1)
#print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
