from datetime import date
from time import sleep
maiores = 0
menores = 0

for i in range(1, 8):
    nascimento = int(input('Informe a sua data de nascimento: '))
    if date.today().year - nascimento < 18:
        menores += 1
    else:
        maiores += 1
print('Analisando os dados...')
sleep(2)
print(f'No total existem {menores} pessoas menores de idade e {maiores} pessoas maiores de idade')
