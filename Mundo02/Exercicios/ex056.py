from time import sleep
media_idade = 0.0
mulheres_menores = 0
homem_mais_velho = ''
quantidade_pessoas = 0
idade_homem_mais_velho = 0

for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Informe o seu nome: ')).strip()
    idade = int(input('Informe a sua idade: '))
    media_idade+= idade
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
    quantidade_pessoas+= 1

    if sexo == 'M':
        if i == 1:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
        else:
            if idade > idade_homem_mais_velho:
                homem_mais_velho = nome
                idade_homem_mais_velho = idade
    elif sexo == 'F':
        if idade < 20:
            mulheres_menores+= 1
    else:
        print('Sexo inválido, tente novamente!')        
print('Analisando os dados...')
sleep(2)
print('O nome do homem mais velho tem {} anos e se chama: {}'.format(idade_homem_mais_velho, homem_mais_velho))
print('A média de idade do grupo foi de {} anos'.format(media_idade/quantidade_pessoas))
print('Mo grupo exitem {} mulheres com menos de 20 anos'.format(mulheres_menores))
