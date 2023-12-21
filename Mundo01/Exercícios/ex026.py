palavra = str(input('Digite algo: ')).upper().strip()
print(len(palavra))

print('Existem quantos "a" na frase? {}'.format(palavra.count('A')))
print('A primeira ocorrência acontece na posição {}'.format(palavra.find('A')))
print('A última ocorrência acontece na posição {}'.format(palavra.rfind('A')))
