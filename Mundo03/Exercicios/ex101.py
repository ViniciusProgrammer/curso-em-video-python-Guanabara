from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'
nascimento = int(input('Informe o seu ano de nascimento: '))
resposta = voto(nascimento)
print('-='*20)
print(resposta)
print('-='*20)
