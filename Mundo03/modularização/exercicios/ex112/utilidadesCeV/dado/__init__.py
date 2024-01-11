def leiaDinheiro(msg):
    while True:
        m = str(input(msg)).strip()
        m = m.replace(',', '.')

        if m.replace('.', '').isdigit():
            return float(m)
        else:
            print(f'ERRO! {m} não é um preço!')
        