frase = 'Curso em Vídeo Python'

teste = '  Curso em Vídeo Python'

print(len(teste))

teste = teste.lstrip()

print(len(teste))

print(frase.split())

print(frase[3])

print(frase[1:13])

print(frase[:13])

print(frase[13:])

print(frase[1:15:2])

print(frase.count('o'))

print(len(frase))

print(frase[15:])

print(frase[:15])

#dessa forma conseguiriamos mudar a frase
frase = frase.replace('Python', 'Android')

print(frase)

print('Curso' in frase)

print(frase.upper())

print(frase.lower())

print(frase.find('deo'))

print(frase.split())
