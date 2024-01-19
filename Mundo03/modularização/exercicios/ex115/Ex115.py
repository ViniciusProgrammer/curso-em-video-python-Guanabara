'''
Crie um sistema modularizado que permita cadastrar nome e idade
em um arquivo de texto simples.

O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar
todas as pessoas cadastradas.
'''

from arquivo import *
from funcoes import *
from time import sleep

arquivo = 'pessoas.txt'
while True:
    exibeMenu()

    opcao = verificaOpcao('\033[1;32mSua Opção: \033[m')
    sleep(1)
    if opcao == 1:
        lerArquivo(arquivo)
    elif opcao == 2:
        imprimiTexto('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaIdade('Idade: ')
        cadastrarPessoa(arquivo, nome, idade)
    else:
        imprimiTexto('OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS!')
        break