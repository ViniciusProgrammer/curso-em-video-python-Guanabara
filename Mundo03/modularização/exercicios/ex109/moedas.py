def aumentar(n, s=False):
    n = n + (n * 0.1)
    if s is True:
        f = moeda(n)
        return f
    else:
        return n
def diminuir(n, s=False):
    n = n - (n * 0.13)
    if s is True:
        f = moeda(n)
        return f
    else:
        return n
def dobro(n, s=False):
    n = 2 * n
    if s is True:
        f = moeda(n)
        return f
    else:
        return n
def metade(n, s=False):
    n = n / 2
    if s is True:
        f = moeda(n)
        return f
    else:
        return n
def moeda(n):
    n = f'\033[32mR${n:.0f},00\033[m'
    return n
