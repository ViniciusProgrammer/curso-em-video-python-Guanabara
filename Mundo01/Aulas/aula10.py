tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---fim---')

nome = str(input('Digite o seu nome: '))

if (nome) == 'Vinicus':
    print('O nome digitado foi {}'.format(nome))
else:
    print('O nome digitado foi {}'.format(nome))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('PARABÉNS' if(media >= 6.0) else 'ESTUDE MAIS')
