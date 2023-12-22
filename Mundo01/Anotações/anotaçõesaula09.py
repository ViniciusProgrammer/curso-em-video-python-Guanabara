'''
Técnifca de Fatiamento de String em Python

O fatiamento em python consiste em pegar um pedaço da string de um ponto inicial até um ponto final.

Considere a seguinte string:
frase = 'Curso em Vídeo Python'

Se usarmos o comando print(frase[9]) o resultado será a letra 'V' pois o comando

se quisermos pegar um pedaço de uma string usamos por exemplo:
print(frase[9:13]) o resultado será 'Víde' pois o comando vai do 9 até o 12, pois o 13 não é incluído.
É sempre uma posição a menos no final.

outro exemplo:

print(frase[9:21:2]) o resultado seria VdoPto pois ele vai do 9 até o 20 pulando de 2 em 2.
lembrnado que a casa 21 não é incluída.

print(frase[:5]) o resultado seria 'Curso' pois ele vai do início até o 4, pois o 5 não é incluído.
pois eu estiu omitindo o início. então ele vai do início até o 4.

Da mesma forma se eu omitir o final:
print(frase[15:]) o resultado seria 'Python' pois ele vai do 15 até o final.

print(frase[9::3]) o resultado seria 'VePh' pois ele vai do 9 até o final pulando de 3 em 3.


Analise de string

Função len() para contar caracteres e saber o tamanho de uma string.:
len(frase) o resultado seria 21 pois ele conta quantos caracteres tem na string.

Função count() para contar quantas vezes aparece um caractere na string.:

print(frase.count('o')) o resultado seria 3 pois ele conta quantas vezes aparece a letra 'o' na string.

Contagem com fatiamento:

o fatiamento vai da posição 0 até o 12, pois o 13 não é incluído e contando quantas vezezo 'o' esta presente nesse espaço.
print(frase.count('o', 0, 13)) o resultado seria 1 pois ele conta quantas vezes aparece a letra 'o' na string do 0 até o 12.

print(frase.find('deo')) o resultado seria 11 pois ele vai procurar a palavra 'deo' na string e vai me retornar a posição onde ela começa.

A funçao find caso a palavra não exista na string ela irá retornar -1.
Exemplo:
print(frase.find('Android')) o resultado seria -1 pois ele vai procurar a palavra 'Android' na string e vai me retornar -1.

usando o operador 
'curso' in frase o resultado seria True pois ele vai procurar a palavra 'curso' na string e vai me retornar True ou False.

Transformação de string:

usando o metodo replace

print(frase.replace('Python', 'Android')) o resultado seria 'Curso em Vídeo Android' pois ele vai substituir a palavra 'Python' por 'Android' na string.
ELe susbstitui apenas na hora de imprimir, não altera a string original.

Letras maiúsculass
print(frase.upper()) o resultado seria 'CURSO EM VÍDEO PYTHON' pois ele vai colocar todas as letras em maiúsculas.

Letras minúsculas
print(frase.lower()) o resultado seria 'curso em vídeo python' pois ele vai colocar todas as letras em minúsculas.

Colocar a primeira letra de cada palavra em maiúscula

print(frase.capitalize()) o resultado seria 'Curso em vídeo python' pois ele vai colocar a primeira letra de cada palavra em maiúscula.
Colocar somente a primeira letra da frase em maiúscula

print(frase.title()) o resultado seria 'Curso Em Vídeo Python' pois ele vai colocar a primeira letra de cada palavra dentro da frase em maiúscula.
tittle é mais ao pé da letra, ele vai colocar a primeira letra de cada frase em maiúscula.

print(frase.strip()) o resultado seria 'Curso em Vídeo Python' pois ele vai remover os espaços inúteis no início e no final da string.
caso precise

print(frase.rstrip()) o resultado seria 'Curso em Vídeo Python' pois ele vai remover os espaços inúteis no final da string. plea direita

print(frase.lstrip()) o resultado seria 'Curso em Vídeo Python' pois ele vai remover os espaços inúteis no início da string. pela esquerda


Divisão de string

print(frase.split()) o resultado seria ['Curso', 'em', 'Vídeo', 'Python'] pois ele vai dividir a string em uma lista de strings.
Ele gera basicamente uma lista com as palavras da string. e cada palavra recebe um indice do inicio ate o final da frase e cada palavra é uma string.


print('-'.join(frase)) o resultado seria 'C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n' pois ele vai juntar a string separando por um traço.
Ele junta a string separando por um traço.

#Uma forma de imprmir uma string inteira

print(""" Nessa aula, vamos aprender operações com String no Python. 
      As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), 
      transformações com replace(), upper(), lower(), capitalize(), 
      title(), strip(), junção com join().""")

Uma string é imultável, ou seja, não pode ser alterada.

se quisermos mudar uma string, podemos fazer o seguinte:

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase) o resultado seria 'Curso em Vídeo Android' pois ele vai substituir a palavra 'Python' por 'Android' na string.


'''