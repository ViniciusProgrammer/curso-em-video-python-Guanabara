n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
soma = n1 + n2
print(type(n1))
print(type(n2))
print('A soma vale', soma)
#Dessa forma acima o que ocorre é a concatenação, pois o input sempre retorna uma string

#Para somarmos os dois valores precisamos incluir o int() na frente do input

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(type(n1))
print(type(n2))
soma = n1 + n2
print('A soma vale {}'.format(soma))
print('A soma entre {} e {} vale {}'.format(n1, n2, n1 + n2)) #Outra forma que funciona

n = float(input('Informe um valor: ')) #exemplo de um valor de ponto flutuante
print(n)
print(type(n)) #clas float

b = input('Digite algo: ')
print(b.isalpha()) #isalpha() é um metodo que retorna True ou False se o valor inserido pelo usuario é uma letra
print(b.isnumeric()) #isnumeric() na verdade ele pergunta se o valor inserido pelo usuario pode ser convertido para um valor numerico e retorna True ou False
print(b.isalnum()) #isalnum() pergunta se o valor inserido pelo usuario é alfanumerico e retorna True ou False
