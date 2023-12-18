from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)
print('{:.2f}'.format(hipotenusa)) 
#sem importar nada
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
#importando a função hypot
print('A hipotenusa vai medir {:.2f}'.format(hypot(cateto_oposto, cateto_adjacente)))
