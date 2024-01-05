times = ('Palmeiras', 'Gremio', 'Atletico-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Atletico-PR', 'Internacional', 'Fortaleza',
         'Sao Paulo', 'Cuiaba', 'Corithians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos',
         'Goias', 'Curitiba', 'America-MG')
print('Os 5 primeiros colocados do brasileirão são')
for i in range(0, 5):
    print(times[i])
print('\nOs últimos 4 colocados do brasileirão são')
for i in range(16, 20):
    print(times[i])
print('\nTimes em ordem alfabética')
print(f'{sorted(times)}')
print(f'O flamego está na {times.index("Flamengo")+1}ª posição')
