def area(l, c):
    print(f'Com as dimensões {l} x {c}')
    print(f'Teremos {l * c :.1f}m² de área.')

largura = float(input('Informe a largura: '))
comprimento = float(input('Informe o comprimento: '))
area(largura, comprimento)
