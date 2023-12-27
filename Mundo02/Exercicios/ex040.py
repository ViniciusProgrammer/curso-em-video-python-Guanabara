nita1 = float(input('Informe a primeira nota: '))
nita2 = float(input('Informe a segunda nota: '))
media = (nita1 + nita2) / 2

if media < 5.0:
    print('Com as notas {:.1f} e {:.1f}, você obteve {:.1f} de média'.format(nita1, nita2, media))
    print('Você está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('Com as notas {:.1f} e {:.1f}, você obteve {:.1f} de média'.format(nita1, nita2, media))
    print('Você está de RECUPERAÇÃO!')
else:
    print('Com as notas {:.1f} e {:.1f}, você obteve {:.1f} de média'.format(nita1, nita2, media))
    print('Parabéns')
    print('Você está APROVADO!')
