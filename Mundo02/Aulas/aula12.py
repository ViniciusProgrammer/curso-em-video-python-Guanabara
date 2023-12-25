nome = str(input('Digitite o seu nome: '))

if nome == 'Vinicius':
    print('QUe nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}!',format(nome))
