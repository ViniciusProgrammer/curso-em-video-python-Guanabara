'''
Aula 20 - Funções (Parte 1)

Exemplo de dec;açao de função:

def mosstrarLinha():
    print('-' * 30)

mosstrarLinha()
print('   CURSO EM VÍDEO   ')
mosstrarLinha()
print('   APRENDA PYTHON   ')
mosstrarLinha()
print('   GUSTAVO GUANABARA   ')
mosstrarLinha() 

Trabalhando com função com parâmetro:

Exemplo com tamanho da linha adpatável ao tamanho da mensagem:

def mensagem(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))
for i in range(0, 3):
    txt = str(input('Insira uma mensagem: '))
    mensagem(txt)
    if i == 2:
        print('Acabou!')

        
Empacotamento de parâmetros:
Funciona da seguinte forma, a função não sabe quantos parâmetros serão passados, então ela empacota todos os parâmetros em uma tupla.
usando o * antes do parâmetro, ele empacota todos os parâmetros em uma tupla.

def contador(* num):

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

'''
