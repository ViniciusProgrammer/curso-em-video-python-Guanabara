'''
Exemplos dos operandos aritméticos

A soma = 5 + 2 = 7
A subtração = 5 - 2 = 3
A multiplicação = 5 * 2 = 10
A divisão = 5 / 2 = 2.5
A Divisão inteira = 5 // 2 = (5 // 2) = 2
O resto da divisão = 5 % 2  = (5 % 2) = 1
A potência = 5 ** 2 (5 elevado a 2) = 25

Esses são os operadores aritméticos usados na linguagem Python
'''

#Aqui a multiplicação tem prioridade diante da soma
n = 5 + 3 * 2
print(n)

#Aqui a potenciação tem prioridade diante da multiplicação e da soma
n = 3 * 5 + 4 ** 2
print(n)

#Aqui os parenteses tem prioridade diante da potenciação e da multiplicação
n = 3 * (5 + 4) ** 2
print(n)

nome = input('Qual é o seu nome: ')
print('Prazer em te conhecer {:>20}!'.format(nome)) #Aqui o nome será alinhado a direita com 20 espaços
print('Prazer em te conhecer {:<20}!'.format(nome)) #Aqui o nome será alinhado a esquerda com 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome)) #Aqui o nome será centralizado com 20 espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Aqui o nome será centralizado com 20 espaços e preenchido com o caracter '='

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma vale {}'.format(n1+n2))
print('A subtração vale {}'.format(n1-n2))
print('A multiplicação vale {}'.format(n1*n2))
print('A divisão vale {}'.format(n1/n2))
print('A divisão inteira vale {}'.format(n1//n2))
print('O resto da divisão vale {}'.format(n1%n2))
print('A potência vale {}'.format(n1**n2))

#Aqui a divisão será feita com 3 casas decimais
print('A divisão vale {:.3f}'.format(n1/n2))
