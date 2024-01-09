jogador = {}
gols = []
jogadores = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
