'''
Operadores aritméticos

Exemplos dos operandos aritméticos

A soma = 5 + 2 = 7
A subtração = 5 - 2 = 3
A multiplicação = 5 * 2 = 10
A divisão = 5 / 2 = 2.5
A Divisão inteira = 5 // 2 = (5 // 2) = 2
O resto da divisão = 5 % 2  = (5 % 2) = 1
A potência = 5 ** 2 (5 elevado a 2) = 25

Esses são os operadores aritméticos usados na linguagem Python

Precedência de operadores:

1º = () os colchetes são os elementos mais importantes dentro de uma expressão aritmética
2º = ** potência
3º = * / // % multiplicação, divisão, divisão inteira e resto da divisão, quem aparecer priemiro na expressão será executado primeiro
4º = + - soma e subtração por ultimo


Na linguagem python temos que o calculo de valores numericos não possuem limite como em outras linguagens,
aliás temos sim limtes que varia de acordo como o tamanho da memória do computador.

Potenciação em python:

4 ** 3 = 64
ou podemos usar a função pow() que é uma função embutida na linguagem python
pow(4, 3) = 64 porém aqui se perde a ordem de precedência de operadores.

Raiz quadrada em python:
podemos fazer da seguinte forma também

81 ** (1/2) = 9

resto da divis~çao em python:

18 % 2 = 0 sobra 0

A divisão com a quantidade de casas decimais o programador pode definir quantas casas decimais ele quer que apareça

n1 = 4
n2 = 3

print('A divisão entre {} e {} é igual a {:.3f}'.format(n1, n2, n1/n2)) nesse caso utilizei 3 casas decimais

end='' é um parametro que serve para não quebrar a linha
\n nao quebra a linha, mas sim pula uma linha

'''