nome = str(input('Digite o seu nome completo: ')).strip()
print(nome.split())
print(len(nome.split()))

print('Muito prazer em te conhecer!')
print('Seu primeito nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))
