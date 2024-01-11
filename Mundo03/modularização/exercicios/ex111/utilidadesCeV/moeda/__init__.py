def moedas(m):
    return (f'R${m:.2f}')


def aumentar(moeda, porcentagem, form=False):
    moeda = moeda + moeda * (porcentagem / 100)

    if form:
        return moedas(moeda)

    return moeda


def diminuir(moeda, porcentagem, form=False):
    moeda = moeda - moeda * (porcentagem / 100)

    if form:
        return moedas(moeda)

    return moeda


def dobro(moeda, form=False):
    moeda = moeda * 2

    if form:
        return moedas(moeda)

    return moeda


def metade(moeda, form=False):
    moeda = moeda / 2

    if form:
        return moedas(moeda)

    return moeda


def resumo(preco, aumento, reducao):

    print('-' * 32)
    print('        RESUMO DO VALOR')
    print('-' * 32)
    
    print(f'Aumentando {aumento}%, temos {aumentar(preco, aumento, True)}')
    print(f'Diminuindo {reducao}%, temos {diminuir(preco, reducao, True)}')
    print(f'O dobro de {moedas(preco)} é {dobro(preco, True)}')
    print(f'A metade de {moedas(preco)} é {metade(preco, True)}')

    print('-' * 32)
