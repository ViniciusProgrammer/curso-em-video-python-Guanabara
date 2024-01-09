from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
