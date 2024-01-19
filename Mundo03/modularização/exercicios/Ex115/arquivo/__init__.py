def verificaArquivo(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
        criarArquivo(nome)
        lerArquivo(nome)
    else:
        print('-' * 50)
        print('{: ^50}'.format('PESSOAS CADASTRADAS'))
        print('-' * 50)
        for l in arq:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arq.close()


def cadastrarPessoa(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print(f'Erro ao tentar abrir o arquivos "{arq}"!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados no arquivo!')
        else:
            print('\033[1;32mDados adicionados com sucesso!\033[m')
            a.close()
