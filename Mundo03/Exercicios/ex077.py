frutas = ('abacate', 'milho', 'laranja',
            'morango', 'banana', 'melancia', 'goiaba',
            'manga', 'abacaxi', 'caju', 'uva', 'pera')
for i in frutas:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\n')
