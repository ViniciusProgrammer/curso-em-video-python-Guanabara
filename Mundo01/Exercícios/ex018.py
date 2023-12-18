from math import sin, cos, tan, radians
angulo = float(input('Informe um angulo: '))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan(radians(angulo))))
