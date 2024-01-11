from ex108 import moedas
n = float(input('Digite um preço: R$'))
print(moedas.moeda(n))
print(f'{n} com aumento de 10% é igual a {moedas.moeda(moedas.aumentar(n, 10))}')
print(f'{n} menos 10% é igual a {moedas.moeda(moedas.diminuir(n, 10))}')
print(f'O dobro de {n} é igual a {moedas.moeda(moedas.dobro(n))}')
print(f'A metade de {n} é igual a {moedas.moeda(moedas.metade(n))}')