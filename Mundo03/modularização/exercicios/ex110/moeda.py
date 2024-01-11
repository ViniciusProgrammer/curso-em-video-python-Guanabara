def aumentar(n, a):
    n = n + (n * (a / 100))
    return n
def diminuir(n, d):
    n = n - (n * (d / 100))
    return n
def dobro(n):
    n = 2 * n
    return n
def metade(n):
    n = n / 2
    return n
def moeda(n):
    n = f'\033[32mR${n:.0f},00\033[m'
    return n
def resumo(v, p1, p2):
    print(30 * '-')
    print('     RESUMO DO VALOR')
    print(30 * '-')
    print(f'Preço analisado:    {moeda(v)}')
    print(f'Dobro do preço:     {moeda(dobro(v))}')
    print(f'Metade do preço:    {moeda(metade(v))}')
    print(f'{p1}% de aumento:     {moeda(aumentar(v, p1))}')
    print(f'{p2}% de redução:     {moeda(diminuir(v, p2))}')
    print(30 * '-')
    