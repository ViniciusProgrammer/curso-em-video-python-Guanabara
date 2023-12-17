preco = float(input('Informe o preço inicial do produto: R$ '))
desconto = preco * (5/100)
print('O novo valor do produto com desconto de 5% é igual a R${:.2f}'.format(preco - desconto))
