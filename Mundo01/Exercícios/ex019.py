import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4] # Cria uma lista com os nomes dos alunos, lista no Python é dessa forma
escolhido = random.choice(lista) # Escolhe um item aleatório de uma lista (random.choice) que pega alguem aleatório dentro da lista
print('O aluno escolhido foi {}'.format(escolhido))
